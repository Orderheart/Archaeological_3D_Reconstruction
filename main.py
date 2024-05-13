import datetime
import shutil
# ///////////////////////////////////////////////////////////////
import sys
import os
import threading

# from modules import Settings

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
import sys
from PySide6.QtCore import QThread, Slot, Signal
import platform
import subprocess
import paramiko
from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from PyQt5 import QtCore
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
import tarfile

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class WorkerThread(QThread):
    # 定义一个信号，用于在脚本运行完成后发送消息
    finished = Signal(str)
    output = Signal(str)  # 确保这一行存在
    error = Signal(str)  # 确保这一行存在

    def __init__(self, command):
        QThread.__init__(self)
        self.command = command

    def run(self):
        # Start the process and capture output
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, bufsize=1,
                                   universal_newlines=True)

        # Loop to capture stdout output in real-time
        stdout_thread = threading.Thread(target=self.capture_output, args=(process.stdout, self.output))
        stderr_thread = threading.Thread(target=self.capture_output, args=(process.stderr, self.error))

        # Start both threads
        stdout_thread.start()
        stderr_thread.start()

        # Wait for the process to finish and threads to terminate
        return_code = process.wait()
        stdout_thread.join()
        stderr_thread.join()

        if return_code:
            # Process failed, but errors are already emitted by the stderr thread
            pass
        else:
            # Process finished successfully
            self.finished.emit("转换完成!")

    def capture_output(self, stream, emit_signal):
        while True:
            line = stream.readline()
            if line:
                emit_signal.emit(line)
            else:
                break
        stream.close()


class WorkerThread_ssh(QThread):
    output = Signal(str)  # 用于发送命令的标准输出
    error = Signal(str)  # 用于发送命令的标准错误
    finished = Signal()  # 用于通知命令执行完成

    def __init__(self, local_dir, remote_dir, hostname, port, username, password):
        QThread.__init__(self)
        self.local_dir = local_dir
        self.remote_dir = remote_dir
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def run(self):
        # 这个函数将在 SFTP 上传过程中被调用
        def sftp_progress_callback(transferred, total):
            # 计算以MB为单位的已传输和总字节数
            transferred_mb = transferred / (1024 ** 2)
            total_mb = total / (1024 ** 2)
            # 计算进度百分比
            progress_percentage = (transferred / total) * 100
            # 发送信号以更新进度日志，现在使用MB为单位
            self.output.emit(f"已上传 {transferred_mb:.2f} / {total_mb:.2f} MB ({progress_percentage:.2f}%)\n")

        # 创建SSH客户端实例
        ssh = paramiko.SSHClient()
        # 自动接受未知的SSH密钥
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # 连接到服务器
            ssh.connect(self.hostname, port=self.port, username=self.username, password=self.password)
            self.output.emit("SSH connect successfully!")

            # 打包目录，确保文件名是正确的
            local_tar_filename = os.path.basename(self.local_dir) + '.tar.gz'
            tar_path = os.path.join(self.local_dir, local_tar_filename)
            # 在Windows环境中标准化路径
            tar_path = os.path.normpath(tar_path)
            with tarfile.open(tar_path, "w:gz") as tar:
                tar.add(self.local_dir, arcname='.')
            print("tar_path:", tar_path)

            # 创建SFTP客户端并发送文件
            sftp = ssh.open_sftp()
            # 使用正斜杠来构建远程路径，以避免混合路径分隔符的问题
            remote_tar_path = self.remote_dir.rstrip('/') + '/' + os.path.basename(tar_path).replace('\\', '/')
            print("remote_tar_path:", remote_tar_path)

            # 执行带有进度监控的 SFTP 上传
            sftp.put(tar_path, remote_tar_path, callback=sftp_progress_callback)

            sftp.put(tar_path, remote_tar_path)
            sftp.close()
            # 在服务器上执行解压和运行脚本的命令
            data_path = self.remote_dir.rstrip('/') + '/' + os.path.basename(self.local_dir).replace('\\', '/')
            print("data_path:", data_path)

            commands = [
                "source /home/yuyang/anaconda3/bin/activate gaussian_splatting",
                # "source /home/yuyang/anaconda3/etc/profile.d/conda.sh",  # 加载conda环境初始化脚本
                # "conda activate gaussian_splatting",  # 激活conda环境
                "cd /home/yuyang/gaussian-splatting",  # 进入gaussian-splatting目录
                f"mkdir -p {data_path}",
                f"tar -xzf {remote_tar_path} -C {data_path}",
                f"python convert.py -s {data_path}",
                f"python train.py -s {data_path}"
            ]
            command_string = " && ".join(commands)

            stdin, stdout, stderr = ssh.exec_command(command_string, get_pty=True)
            for line in iter(stdout.readline, ""):
                self.output.emit(line)

            error = stderr.read().decode('utf-8')
            if error:
                self.error.emit(error)

            os.remove(tar_path)

            # 关闭SFTP和SSH连接
            sftp.close()
            ssh.close()
            self.finished.emit()
        except Exception as e:
            # 如果发生异常，发送错误消息
            self.error.emit(f"SSH连接失败: {str(e)}")
            # 确保资源被释放
            if 'sftp' in locals():
                sftp.close()
            if 'ssh' in locals():
                ssh.close()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        # 创建了一个Ui_MainWindow对象，这个对象是使用Qt Designer创建的用户界面类，包含了主窗口的布局和各种部件。
        self.ui = Ui_MainWindow()
        # 将主窗口对象self作为参数传递给setupUi()方法，用于设置主窗口的用户界面。
        # 这个方法会将UI设计中的部件添加到主窗口中。
        self.ui.setupUi(self)
        # 声明了一个全局变量widgets，用于在整个应用程序中访问主窗口中的部件。
        global widgets
        # 将Ui_MainWindow对象赋值给全局变量widgets，这样就可以通过widgets对象访问主窗口中的所有部件，
        # 而不需要在每个函数中都传递主窗口对象或者UI对象
        widgets = self.ui
        # 定义一个属性来存储全局的data_dir值
        self.global_data_dir = None
        # 定义一个属性来存储全局的python运行环境值
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "千映"
        description = "千映：基于高斯喷溅的端边云田野考古三维重建系统"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # 在主窗口中的 toggleButton 按钮的点击事件中连接了一个槽函数
        # widgets.toggleButton.clicked.connect(...)：这是一个PyQt中的信号与槽机制。
        # clicked是toggleButton的点击事件信号，
        # .connect(...)用于将这个信号连接到一个槽函数。
        # lambda: UIFunctions.toggleMenu(self, False)：这是一个匿名函数，其作用是调用UIFunctions类中的toggleMenu方法。
        # 匿名函数中的self是指向当前对象，即主窗口对象。
        # False是作为参数传递给toggleMenu方法的，用于控制菜单的显示或隐藏。
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, False))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        # 调用了UIFunctions类中的uiDefinitions方法，用于设置主窗口中的各种部件的样式和功能。
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        # 这段代码将四个按钮（btn_home、btn_widgets、btn_new 和 btn_save）的点击事件连接到同一个槽函数 buttonClick。
        # 这意味着当任何一个按钮被点击时，都会触发 buttonClick 方法。

        # 这样做的好处是可以避免在代码中重复编写相似的逻辑，因为这些按钮可能执行相似的操作或者需要相同的处理。
        # 通过连接到同一个槽函数，可以减少重复代码，使代码更加简洁和易于维护。
        # 在 buttonClick 方法中，可以根据不同的按钮执行不同的操作，以响应不同的用户输入。
        # 例如，可以使用 sender() 方法来确定哪个按钮触发了点击事件，并根据按钮的标识符执行相应的操作。
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.start_train.clicked.connect(self.buttonClick)
        widgets.select_file.clicked.connect(self.select_and_process_media)
        # widgets.start_construction.clicked.connect(self.on_convert_triggered)
        widgets.start_construction.clicked.connect(self.buttonClick)
        widgets.start_setting.clicked.connect(self.buttonClick)
        widgets.model_view.clicked.connect(self.select_out)
        widgets.pushButton.clicked.connect(self.on_connect_ssh_triggered)
        widgets.local_save.clicked.connect(self.buttonClick)
        widgets.ssh_save.clicked.connect(self.buttonClick)
        # Attach signal handlers

        # openCloseLeftBox函数的作用是打开或关闭左侧的额外框。它被连接到了两个按钮的点击事件上：
        # toggleLeftBox和extraCloseColumnBtn。
        # 这意味着无论用户是点击左侧额外框的按钮还是另一个按钮，都会执行相同的操作，
        # 即调用UIFunctions.toggleLeftBox(self, True)方法，以打开或关闭左侧框

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # openCloseRightBox 函数的作用类似，但是针对的是右侧的额外框。它被连接到了 settingsTopBtn 按钮的点击事件上。
        # 这意味着当用户点击右侧框顶部的按钮时，会执行相同的操作，
        # 即调用 UIFunctions.toggleRightBox(self, True) 方法，以打开或关闭右侧框。

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        # Set window size
        # self.resize(2400, 1600)
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        # 这段代码用于在应用程序的堆叠小部件（stackedWidget）中设置当前显示的页面，并高亮显示与当前页面关联的菜单按钮。

        # stackedWidget是一种特殊的小部件，它可以包含多个小部件，但一次只显示其中一个。
        # 这行代码的作用是将stackedWidget当前显示的小部件设置为widgets.home。这通常对应于应用程序中的“主页”或“首页”视图
        widgets.stackedWidget.setCurrentWidget(widgets.home)

        # 这行代码改变了btn_home按钮的样式表。它调用了UIFunctions.selectMenu方法，将按钮当前的样式表作为参数传递进去。
        # UIFunctions.selectMenu方法会返回一个修改过的样式表，用于突出显示菜单按钮，表明它是当前被选中的。
        # 这样做可以为用户提供视觉反馈，说明他们当前正在查看的是哪个页面或部分。
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW TRAINING PAGE
        if btnName == "start_train":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "start_setting":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)
            UIFunctions.resetStyle(self, btnName)

        if btnName == "btn_save":
            print("Save BTN clicked!")

        if btnName == "start_construction":
            print("Start construction BTN clicked!")
            if widgets.local_rebuid.isChecked():
                self.on_convert_triggered()
            elif widgets.cloud_rebuid.isChecked():
                self.on_convert_ssh_triggered()
            else:
                QMessageBox.information(self, "Information", "请选择模型重建方式!")

        if btnName == "local_save":
            print("Local save BTN clicked!")
            widgets.setting_log.appendPlainText("本地保存配置成功!")

        if btnName == "ssh_save":
            print("SSH save BTN clicked!")
            widgets.setting_log.appendPlainText("SSH保存配置成功!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # 重新调整大小
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # 设置拖动窗口
        self.dragPos = event.globalPos()

        # 打印鼠标事件
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    # ///////////////////////////////////////////////////////////////
    def select_out(self):
        print("Select_out clicked!")
        # 设置文件对话框以选择文件夹
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.Directory)
        # file_dialog.setOption(QFileDialog.ShowDirsOnly, True)

        # 设置默认打开的目录
        default_dir = "F:/3D_gaussian_splatting/gaussian-splatting/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/output"
        file_dialog.setDirectory(default_dir)

        if file_dialog.exec():
            selected_folder = file_dialog.selectedFiles()[0]
            print("Selected folder:", selected_folder)
            self.run_batch_script(selected_folder)

    def  run_batch_script(self, directory):
        # 构建批处理文件命令
        script_path = "./scripts/run_viewmodel.bat"  # 脚本路径
        command = f'"{script_path}" "{directory}"'
        print("Executing batch script:", command)
        # 执行批处理文件

        subprocess.run(command, shell=True, check=True)
    # ///////////////////////////////////////////////////////////////
    # 打开文件选择器，选择照片集合或视频
    def select_and_process_media(self):
        print("Select_and_process_media clicked!")
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.process_files(selected_files)
    # ///////////////////////////////////////////////////////////////
    def on_connect_ssh_triggered(self):
        # 创建SSH客户端实例
        ssh = paramiko.SSHClient()
        # 自动接受未知的SSH密钥
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # 连接到服务器
            hostname_ssh = widgets.lineEdit_2.text()
            port_ssh = 22
            username_ssh = widgets.lineEdit_4.text()
            password_ssh = widgets.lineEdit_5.text()
            ssh.connect(hostname=hostname_ssh, port=port_ssh, username=username_ssh, password=password_ssh)
            print("SSH连接成功!")
            widgets.setting_log.appendPlainText("远程服务器连接成功!")
        except Exception as e:
            widgets.setting_log.appendPlainText(f"连接失败: {str(e)}")
    # ///////////////////////////////////////////////////////////////
    def process_files(self, files):
        # 获取当前时间并格式化为年-月-日-时-分-秒
        time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        data_dir = f"./data/{time_str}/input"
        os.makedirs(data_dir, exist_ok=True)
        photo_names = []  # 用于存储复制的照片名称
        total_size = 0  # 初始化照片的总占用空间
        for file_path in files:
            # 获取文件名
            base_name = os.path.basename(file_path)
            # 目标路径
            target_path = os.path.join(data_dir, base_name)

            # 检查文件类型并分别处理
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # 照片文件，直接复制
                shutil.copy(file_path, target_path)
                photo_names.append(base_name)
                # 累加文件大小
                total_size += os.path.getsize(target_path)

        # 计算总占用空间（MB）和平均占用空间（MB）
        total_size_mb = total_size / (1024 ** 2)
        average_size_mb = total_size_mb / len(photo_names) if photo_names else 0

        # 将复制的照片名称写入到主UI界面上的QPlainTextEdit
        widgets.plainTextEdit.setPlainText("\n".join(photo_names))
        # 去掉路径末尾的/input，确保跨平台兼容性
        data_dir = os.path.split(data_dir)[0]
        # 将修改后的data_dir赋值给全局变量
        self.global_data_dir = data_dir
        print(f"Data directory: {self.global_data_dir}")

        widgets.lineEdit.setText(data_dir)
        # 如果复制了照片，则显示一个消息框
        if photo_names:
            QMessageBox.information(self, "Information", "照片成功选择!")
            # 设置QTextEdit控件显示照片数量及其占用空间信息
            photo_count_text = (f"照片数量: {len(photo_names)}\n"
                                f"总占用空间: {total_size_mb:.2f} MB\n"
                                f"平均占用空间: {average_size_mb:.2f} MB")
            widgets.photo_sum.setPlainText(photo_count_text)
        else:
            QMessageBox.information(self, "Information", "没有照片被选择.")

    @Slot(str)
    def append_output(self, text):
        widgets.log.appendPlainText(text)

    @Slot(str)
    def append_error(self, text):
        widgets.log.appendPlainText(text)

    @Slot(str)
    def append_ssh_output(self, text):
        widgets.plainTextEdit.appendPlainText(text)

    @Slot(str)
    def append_ssh_error(self, text):
        widgets.plainTextEdit.appendPlainText(text)

    @Slot(str)
    def on_conversion_finished(self, message):
        # Handle the completion of the conversion process
        QMessageBox.information(self, "Information", message)

    @Slot()
    def on_conversion_finished(self):
        QMessageBox.information(self, "Information", "Command execution finished!")


    @Slot()
    def on_convert_triggered(self):
        print("button start construction clicked!")
        # 创建后台线程对象
        print("recent global_data_dir: ", self.global_data_dir)

        # 设置响应脚本的路径
        bat_script = "./scripts/run_gaussian_splatting.bat"
    
        command = f'cmd.exe /c ""{bat_script}" "{self.global_data_dir}""'

        # 创造工作流
        self.worker_thread = WorkerThread(command)
        self.worker_thread.output.connect(self.append_output)
        self.worker_thread.error.connect(self.append_error)
        self.worker_thread.finished.connect(self.on_conversion_finished)
        self.worker_thread.start()

    # SSH服务器重建
    def on_convert_ssh_triggered(self):
        print("button start construction ssh clicked!")
        # 创建后台线程对象
        # 清空 plainTextEdit 的内容
        widgets.plainTextEdit.clear()

        print("recent global_data_dir: ", self.global_data_dir)
        self.worker_thread = WorkerThread_ssh(
            local_dir=self.global_data_dir,
            remote_dir='/home/yuyang/gaussian-splatting/data',
            hostname='10.147.17.109',
            port=22,
            username='yuyang',
            password='yuyang'
        )
        self.worker_thread.output.connect(self.append_ssh_output)
        self.worker_thread.error.connect(self.append_ssh_error)
        self.worker_thread.finished.connect(self.on_conversion_finished)
        self.worker_thread.start()  # 启动线程


if __name__ == "__main__":
    # 在创建 QApplication 实例之前启用高 DPI 缩放
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
