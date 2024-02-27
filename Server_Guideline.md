# Ubuntu配置

## 一.配置显卡驱动

### 1.更新软件列表和安装必要依赖

```
sudo apt update
sudo apt install g++
sudo apt install gcc
sudo apt install make
```

更新rz服务便于windows上传文件到服务器

```
apt-get install lrzsz
```

启动为

```
rz
```

### 2.查询当前显卡信息

使用指令查询当前机器的版本情况

```
lsb_release -a
```

使用指令查询当前机器的显卡情况

```
lspci | grep VGA
```

使用指令查询最佳的NVIDIA显卡驱动

```
cat /proc/driver/nvidia/version
```

最后一条指令输出如下:

![image-20240227102624601](Ubuntu配置.assets/image-20240227102624601.png)

故应该使用53.54.03版本的nvidia显卡驱动



前往NVIDIA官网找到对应版本和显卡的驱动，下载后使用`rz`上传到服务器 

NVIDIA驱动下载：https://www.nvidia.cn/Download/index.aspx?lang=cn

创建一个放置各种包的文件夹

```
mkdir linux_packages
cd linux_packages
```

选择准备上传的驱动

```
rz
```





### 3.禁用系统自带的显卡驱动nouveau

在终端输入命令打开blacklist.conf文件。

```bash
sudo vim /etc/modprobe.d/blacklist.conf
```

在打开的文件末尾输入并保存：

```
blacklist nouveau
options nouveau modeset=0
```


最后更新一下系统的initramfs镜像文件，在终端中输入：

```
sudo update-initramfs -u
```


完成以上步骤后，重启电脑。然后在终端中输入：

```
lsmod | grep nouveau
```


如果没有输出的话就说明禁用了nouveau。



### 4.安装gdm3

停止当前的显示服务器。如果进不去，就按Ctrl + Alt + F2~F6中的一个 (分别对应进入tty2~tty6)）（必须）

```
sudo telinit 3
```

cd命令进入到你存放驱动的目录`linux_packages`，执行以下指令

```
sudo chmod 777 NVIDIA-Linux-x86_64-535.54.03.run   #给你下载的驱动赋予可执行权限，才可以安装
sudo ./NVIDIA-Linux-x86_64-535.54.03.run --no-opengl-files --no-x-check #安装
```

sudo sh nvidia.run --add-this-kernel

-no-x-check：安装驱动时关闭X服务

-no-nouveau-check：安装驱动时禁用nouveau

-no-opengl-files：只安装驱动文件，不安装OpenGL文件

-add

显卡驱动安装过程中一些选项：
1.The distribution-provided pre-install script failed! Are you sure you want to continue?
选择continue installation
剩下全部选no

安装结束后

```
sudo telinit 5
```

### 5.检验显卡驱动

挂载Nvidia驱动：

```
modprobe nvidia
```

输入以下指令，出现显卡信息说明安装成功：

```
nvidia-smi
```

![image-20240225160043634](Ubuntu配置.assets/image-20240225160043634.png)





## 二.配置CUDA环境

### 1.安装CUDAToolkit

为配置3D Gaussian Splatting 的CUDA环境，参考原论文的environment配置如下:

```
name: gaussian_splatting
channels:
  - pytorch
  - conda-forge
  - defaults
dependencies:
  - cudatoolkit=11.8
  - plyfile=0.8.1
  - python=3.7.13
  - pip=22.3.1
  - pytorch=1.12.1
  - torchaudio=0.12.1
  - torchvision=0.13.1
  - tqdm
  - pip:
    - submodules/diff-gaussian-rasterization
    - submodules/simple-knn
```

进入网站https://developer.nvidia.com/cuda-toolkit-archive选择对应版本的CUDA，执行安装

![image-20240225161836672](Ubuntu配置.assets/image-20240225161836672.png)

有可能系统会自动帮你升级到最新的驱动，有的库需要特殊的CUDA版本，所以我们可以更改最后一行命令，来安装指定版本的CUDA，`sudo apt-get -y install cuda-118`

指令集如下：

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```



查找cuda安装路径，添加到环境变量中：

```
ls /usr/local/ | grep cuda
```

![image-20240225164141856](Ubuntu配置.assets/image-20240225164141856.png)

```
sudo vim ~/.bashrc
```

在文件末尾添加：

```
export CUDA_HOME=/usr/local/cuda-11.8
if [[ ":$PATH:" != *":/usr/local/cuda-11.8/bin:"* ]]; then
    export PATH=$PATH:/usr/local/cuda-11.8/bin
fi
if [[ ":$LD_LIBRARY_PATH:" != *":/usr/local/cuda-11.8/lib64:"* ]]; then
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.8/lib64
fi
```

再输入`source ~/.bashrc`来使得更改生效



执行以下指令，如果有输出，则说明安装成功

```
nvcc -V
```

![image-20240225164520334](Ubuntu配置.assets/image-20240225164520334.png)



### 2.安装anaconda/miniconda

为与原论文实验环境一致，这里安装anaconda linux 环境（实际更推荐miniconda，只包含python和conda，更节约内存空间）

在网站：

```
https://repo.anaconda.com/archive/
```

查询需要安装的anaconda版本：

这里以我自己安装的版本为例：

https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh

下载好后从windows端使用`rz`发送到linux下，授予文件权限并安装（本来想wget，但是一直timeout连不上）

```
chmod +777 Anaconda3-2023.09-0-Linux-x86_64.sh
./Anaconda3-2023.09-0-Linux-x86_64.sh
```

一路enter，注意最后要同意协议，输入yes



将conda添加到环境变量中:

```
sudo vim ~/.bashrc
```

添加以下内容到最后一行

```
export PATH=~/anaconda3/bin:$PATH
```

保存后，更新配置

```
source ~./bashrc
```

检查conda指令

```
conda
```

有以下输出则说明安装conda环境完成

![image-20240225171038590](Ubuntu配置.assets/image-20240225171038590.png)



## 三.配置 3D Gaussian Splatting 环境

### 1.源码下载

从原论文界面下载项目源码和子模块：

```
git clone git@github.com:graphdeco-inria/gaussian-splatting.git --recursive
```

配置虚拟环境

```
conda env create --file environment.yml
conda activate gaussian_splatting
```

这里可能存在多个子模块不存在的情况，是因为原作者的recursive链接丢失，需要自己去把丢失的模块给pip一下

### 2.配置渲染器

安装必要的依赖

```
# Dependencies
sudo apt install -y libglew-dev libassimp-dev libboost-all-dev libgtk-3-dev libopencv-dev libglfw3-dev libavdevice-dev libavcodec-dev libeigen3-dev libxxf86vm-dev libembree-dev
# Project setup
cd SIBR_viewers
cmake -Bbuild . -DCMAKE_BUILD_TYPE=Release # add -G Ninja to build faster
cmake --build build -j24 --target install
```

这里`cmake --build build -j24 --target install`会遇到报错，提示需要`CURL_OPENSSL_4`，故考虑重新构建opencv对应版本的库

下载地址：

[Releases · opencv/opencv (github.com)](https://github.com/opencv/opencv/releases)

```
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_easy_getinfo@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_perform@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_cleanup@CURL_OPENSSL_4'
/usr/bin/ld: /lib/x86_64-linux-gnu/libnetcdf.so.19: undefined reference to `curl_global_init@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_mime_init@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_remove_handle@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `std::condition_variable::wait(std::unique_lock<std::mutex>&)@GLIBCXX_3.4.30'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_mime_addpart@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_version_info@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_mime_name@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_mime_filename@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_info_read@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_easy_setopt@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_mime_free@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_easy_cleanup@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_mime_data_cb@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_easy_perform@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_easy_init@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_add_handle@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_slist_free_all@CURL_OPENSSL_4'
/usr/bin/ld: /lib/x86_64-linux-gnu/libnetcdf.so.19: undefined reference to `curl_easy_strerror@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_slist_append@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_poll@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_version@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_setopt@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_mime_data@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_init@CURL_OPENSSL_4'
/usr/bin/ld: /lib/libgdal.so.30: undefined reference to `curl_multi_wait@CURL_OPENSSL_4'
/usr/bin/ld: /lib/x86_64-linux-gnu/libnetcdf.so.19: undefined reference to `curl_global_cleanup@CURL_OPENSSL_4'
collect2: error: ld returned 1 exit status
gmake[2]: *** [src/projects/remote/apps/remoteGaussianUI/CMakeFiles/SIBR_remoteGaussian_app.dir/build.make:187: src/projects/remote/apps/remo
```

下载完成后：

```
tar -zxvf opencv-4.5.tar.gz 
cd opencv-4.5.3
ll

mkdir build
cd build/

cmake ..
make -j16
make install

# 记录编译路径（ CMakeLists.txt 中需要指定该路径 ）：

/build/ownOppenCV/opencv-4.5.3/build
```

然后修改SIBR_viewers里的Cmakelist.txt文件：，指定OpenCV路径

```
 vim CMakeLists.txt 
 # 添加如下：指定编译安装的目录
 set(OpenCV_DIR /build/opencv-4.5.3/build)
 find_package(OpenCV REQUIRED)
```





### 3.安装COLMAP(*)

### **巨坑啊啊啊啊!!!!!踩不完的坑！！！！**

按照官方文档的方法完成COLMAP的编译：

```
https://colmap.github.io/install.html
```

拉取COLMAP的文件：

[colmap/colmap: COLMAP - Structure-from-Motion and Multi-View Stereo (github.com)](https://github.com/colmap/colmap?tab=readme-ov-file)



安装Ceres优化库,这个库要和colmap在一个目录下！！！！

**注意2.2.0的版本需要C++ 17！！！！！其他版本的或多或少有问题！！！！！！！！！！！！！！！！！**

**千万不要从github里拉取ceres！！！！！！！！！！不然会变得不幸！！！！！！！！！**

```
sudo apt-get install libatlas-base-dev libsuitesparse-dev
# 在这里下载ceres:  http://distfiles.macports.org/ceres-solver/

cd ceres-solve-2.2.0
mkdir build
cd build
cmake .. -DBUILD_TESTING=OFF -DBUILD_EXAMPLsES=OFF
make -j
sudo make install
```

**注意，这里可能会与anaconda3/lib发生冲突，解决方法是先把anaconda3文件夹改个名字，然后make install完了之后再改回来**

**报错：**

```
CMake Error at cmake/FindTBB.cmake:224 (file):
  file failed to open for reading (No such file or directory):

    /usr/include/tbb/tbb_stddef.h
Call Stack (most recent call first):
  cmake/FindSuiteSparse.cmake:294 (find_package)
  CMakeLists.txt:266 (find_package)
```

ceres的依赖项tbb库中tbb_stddef.h文件包含了tbb库的版本信息，但已从tbb 2021.1版中删除。相同目录下的version.h有相似内容。

进入cmake/FindTBB.cmake,替换 `tbb/tbb_stddef.h` 为 `tbb/version.h`，则构建没有任何错误



安装CUDA package 和GCC

```
sudo apt-get install gcc-10 g++-10
export CC=/usr/bin/gcc-10
export CXX=/usr/bin/g++-10
export CUDAHOSTCXX=/usr/bin/g++-10
```

安装其他依赖

```
sudo apt-get install \
    git \
    cmake \
    ninja-build \
    build-essential \
    libboost-program-options-dev \
    libboost-filesystem-dev \
    libboost-graph-dev \
    libboost-system-dev \
    libeigen3-dev \
    libflann-dev \
    libfreeimage-dev \
    libmetis-dev \
    libgoogle-glog-dev \
    libgtest-dev \
    libsqlite3-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev \
    libceres-dev
```

#set(CMAKE_CUDA_ARCHITECTURES "native") 注意这里的native，有些机器会报错，那么就修改到对应机器显卡的architecture，如RTX 2080Ti 是 75

```
git clone https://github.com/colmap/colmap.git
cd colmap
mkdir build
cd build
# 插入CMakeList.txt：    set(CMAKE_CUDA_ARCHITECTURES "native")
# 插入CMakeList.txt:    set(CMAKE_CXX_STANDARD 17)
                       set(CMAKE_CXX_STANDARD_REQUIRED ON)
cmake ..
make -j8
sudo make install
```

```
set(CMAKE_CUDA_ARCHITECTURES "native")
#因为ceres的编译环境需要C++ 17）
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
```



来自COLMAP原文：

Or, manually install latest CUDA from NVIDIA’s homepage. During CMake configuration specify CMAKE_CUDA_ARCHITECTURES as “native”, if you want to run COLMAP on your current machine only, “all”/”all-major” to be able to distribute to other machines, or a specific CUDA architecture like “75”, etc.

**报错：**

```
CMake Error at /usr/share/cmake-3.22/Modules/CMakeDetermineCompilerId.cmake:726 (message):
  Compiling the CUDA compiler identification source file
  "CMakeCUDACompilerId.cu" failed.

  Compiler: /usr/local/cuda-11.8/bin/nvcc

  Build flags:

  Id flags:
  --keep;--keep-dir;tmp;-ccbin=/usr/bin/g++-10;-gencode=arch=compute_,code=sm_
  -v

  

  The output was:

  1

  nvcc fatal : Unsupported gpu architecture 'compute_'

  

  

Call Stack (most recent call first):
  /usr/share/cmake-3.22/Modules/CMakeDetermineCompilerId.cmake:6 (CMAKE_DETERMINE_COMPILER_ID_BUILD)
  /usr/share/cmake-3.22/Modules/CMakeDetermineCompilerId.cmake:48 (__determine_compiler_id_test)
  /usr/share/cmake-3.22/Modules/CMakeDetermineCUDACompiler.cmake:298 (CMAKE_DETERMINE_COMPILER_ID)
  CMakeLists.txt:157 (enable_language)

```

查询https://github.com/colmap/colmap/issues/1822得知，某些GPU不能按找官方文档那样设置为native，需要给出具体GPU型号的

architecture，查阅得RTX 2080Ti 的architecture 为 75，故set更改为：

```
set(CMAKE_CUDA_ARCHITECTURES "75") 
```

Cmake 报错完美解决



**报错：**

```
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/10/../../../x86_64-linux-gnu/libfreeimage.so: undefined reference to `TIFFFieldTag@LIBTIFF_4.0'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/10/../../../x86_64-linux-gnu/libfreeimage.so: undefined reference to `TIFFFieldName@LIBTIFF_4.0'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/10/../../../x86_64-linux-gnu/libfreeimage.so: undefined reference to `TIFFFieldReadCount@LIBTIFF_4.0'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/10/../../../x86_64-linux-gnu/libfreeimage.so: undefined reference to `TIFFFieldPassCount@LIBTIFF_4.0'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/10/../../../x86_64-linux-gnu/libfreeimage.so: undefined reference to `TIFFFieldDataType@LIBTIFF_4.0'
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/10/../../../x86_64-linux-gnu/libfreeimage.so: undefined reference to `_TIFFDataSize@LIBTIFF_4.0'
collect2: error: ld returned 1 exit status
make[2]: *** [src/exe/CMakeFiles/colmap_exe.dir/build.make:274: src/exe/colmap] Error 1
make[1]: *** [CMakeFiles/Makefile2:665: src/exe/CMakeFiles/colmap_exe.dir/all] Error 2
make: *** [Makefile:136: all] Error 2

```

出现原因主要是系统中存在的 tiff 版本与编译需要的版本不一致导致的。出现上述报错undefined reference to TIFFReadDirectory@LIBTIFF_4.0 是因为编译程序需要的是 tiff-4.0 版本，但是系统内的不是这个版本。
安装方法：
libtiff官网:https://download.osgeo.org/libtiff/下载对应的安装包 tiff-4.0.10.zip,(tiff-4.0.x.zip 都可以)，解压之后，然后编译安装

 ```
 cd tiff-4.0.10/
 mkdir cmake-build
 cd cmake-build/
 cmake ..
 make
 sudo make install
 ```



然后就编译过了！！！这里省略了各种切换版本和试错的环节（（（（（（



# 3D Gaussian Splatting 训练

总结下来操作就是：

备好数据集。数据集专门放到data文件夹，照片数据结构如下：

![image-20240227131741168](Ubuntu配置.assets/image-20240227131741168.png)

激活环境

````
conda activate gaussian_splatting
````

调用COLMAP计算SFM

````
python convert.py -s ./data/<location> 
````

调用gaussian splatting进行训练

````
python train.py -s ./data/<location> 
````

正常训练

![image-20240227134056540](Ubuntu配置.assets/image-20240227134056540.png)



训练结束的文件保存在data的同一目录下的output文件夹里，调用

```
./<SIBR install dir>/bin/SIBR_gaussianViewer_app -m <path to trained model>
```

即可渲染观看

效果不输photocapture和LUMA ！！！

![image-20240227132804583](Ubuntu配置.assets/image-20240227132804583.png)

文档中说可以remote，后续进行remote测试



