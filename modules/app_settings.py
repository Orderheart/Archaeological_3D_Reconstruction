class Settings():
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    # 这是一个布尔值，用于控制是否启用自定义标题栏。如果设置为True，则启用自定义标题栏；否则，禁用。
    ENABLE_CUSTOM_TITLE_BAR = True
    # 菜单的宽度，以像素为单位。
    MENU_WIDTH = 360
    # 左侧框的宽度，以像素为单位。
    LEFT_BOX_WIDTH = 240
    # 右侧框的宽度，以像素为单位。
    RIGHT_BOX_WIDTH = 240
    # 动画的时间，以毫秒为单位。该属性定义了动画的持续时间。
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    # 左侧框内按钮的背景颜色。这里设置为一种深灰色。
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    # 右侧框内按钮的背景颜色。这里设置为一种粉红色。
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    # 菜单选定状态的样式表。该样式表包含了一个渐变边框和背景颜色。边框的渐变效果由qlineargradient定义，背景颜色设置为一种深灰色。
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """
