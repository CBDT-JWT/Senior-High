from xml.etree.ElementPath import prepare_star
from prefix import *
from os import _exit

global lines_number,columns_number,seats
lines_number=columns_number=0
seats=[]

global data_file_name
data_file_name=""

# 判断test的位置
def IN(test,MIN,MAX):
    if test[0]>MIN[0] and test[0]<MAX[0] and test[1]>MIN[1] and test[1]<MAX[1]:
        return True
    else:
        return False

# 弹出提示
def show_info(event):
    tk=Tk()
    tk.withdraw()
    tk.update()#隐藏tkinter窗口，只显示提示窗口
    showinfo('提示',event)
    tk.destroy()
    return
# 弹出错误
def show_error(event):
    tk=Tk()
    tk.withdraw()
    tk.update()#隐藏tkinter窗口，只显示提示窗口
    showerror('错误',event)
    tk.destroy()
    return
# 弹出文件选择框
def select_file(file_mode): # file_mode 为包含n个元组的列表
    tk=Tk()
    tk.withdraw()
    tk.update()
    file_name=askopenfilename(title="选择文件",
            filetypes=file_mode,initialdir=".\\")
    tk.destroy()
    return file_name

# 欢迎界面
def greet():
    greet_surface=pygame.display.set_mode((500,200))
    pygame.display.set_caption("欢迎")
    greet_surface.fill(GRAY)
    LOADING_BLOCKS=[pygame.Rect(100+30*i,139,30,12) for i in range(10)]
    LOADING_BLOCKS=[""]+LOADING_BLOCKS

    for id in range(1,11):
        greet_surface.fill(GRAY)
        greet_word=FONT.render("欢迎使用随机座位v3.0",True,YELLOW) # 内容、抗锯齿、颜色
        greet_word_rect=greet_word.get_rect()
        greet_word_rect.center=(250,60)
        greet_surface.blit(greet_word,greet_word_rect)
        greet_word=VERY_LITTLE_FONT.render(f"加载中...{id}0%",True,YELLOW) # 内容、抗锯齿、颜色
        greet_word_rect=greet_word.get_rect()
        greet_word_rect.center=(250,120)
        greet_surface.blit(greet_word,greet_word_rect)
        loading_rect=pygame.Rect(95,135,310,20)
        pygame.draw.rect(greet_surface,YELLOW,loading_rect,3)
        for i in range(1,id):
            pygame.draw.rect(greet_surface,YELLOW,LOADING_BLOCKS[i])
        sleep(random.random()/2)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                _exit(0)
        pygame.display.update()
    pygame.display.quit()

# 导入、新建
def import_or_create():
    import_or_create_surface=pygame.display.set_mode((200,200))
    pygame.display.set_caption("导入/新建")
    # 布置界面
    import_button=LITTLE_FONT.render("导入",True,WHITE)
    import_button_rect=import_button.get_rect()
    import_button_rect.center=(100,55)
    create_button=LITTLE_FONT.render("新建",True,WHITE)
    create_button_rect=create_button.get_rect()
    create_button_rect.center=(100,105)
    last_button=LITTLE_FONT.render("最近",True,WHITE)
    last_button_rect=last_button.get_rect()
    last_button_rect.center=(100,155)
    # 维持窗口
    while True:
        import_or_create_surface.fill(GRAY)
        import_or_create_surface.blit(import_button,import_button_rect)
        import_or_create_surface.blit(create_button,create_button_rect)
        import_or_create_surface.blit(last_button,last_button_rect)

        for event in pygame.event.get():
            # 退出
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)
            
            # 鼠标悬停
            if IN(pygame.mouse.get_pos(),import_button_rect.topleft,import_button_rect.bottomright):
                import_button=LITTLE_FONT.render("导入",True,YELLOW)
            else:
                import_button=LITTLE_FONT.render("导入",True,WHITE)
            if IN(pygame.mouse.get_pos(),create_button_rect.topleft,create_button_rect.bottomright):
                create_button=LITTLE_FONT.render("新建",True,YELLOW)
            else:
                create_button=LITTLE_FONT.render("新建",True,WHITE)
            if IN(pygame.mouse.get_pos(),last_button_rect.topleft,last_button_rect.bottomright):
                last_button=LITTLE_FONT.render("最近",True,YELLOW)
            else:
                last_button=LITTLE_FONT.render("最近",True,WHITE)
        
            # 鼠标点击
            if event.type==MOUSEBUTTONUP:
                if IN(pygame.mouse.get_pos(),import_button_rect.topleft,import_button_rect.bottomright):
                    pygame.display.quit()
                    return "import"
                elif IN(pygame.mouse.get_pos(),create_button_rect.topleft,create_button_rect.bottomright):
                    pygame.display.quit()
                    return "new"
                elif IN(pygame.mouse.get_pos(),last_button_rect.topleft,last_button_rect.bottomright):
                    return "last"
        
        pygame.display.update()

# 选择座位行列数
def choose_seats_numbers():
    choose_seats_numbers_surface=Tk()
    choose_seats_numbers_surface.title("设置行列数")
    lines_frame=Frame(choose_seats_numbers_surface)
    # 行
    lines_frame.pack(fill="both")
    lines_label=Label(lines_frame,text="行数：",font=("",12))
    lines_label.pack(fill="both",side="left")
    lines_entry=Entry(lines_frame,font=("",12))
    lines_entry.pack(fill="both",side="right")
    # 列
    columns_frame=Frame(choose_seats_numbers_surface)
    columns_frame.pack(fill="both")
    columns_label=Label(columns_frame,text="列数：",font=("",12))
    columns_label.pack(fill="both",side="left")
    columns_entry=Entry(columns_frame,font=("",12))
    columns_entry.pack(fill="both",side="right")
    # 确定按钮
    def get_seats_number():
        global lines_number,columns_number
        lines_number=lines_entry.get()
        columns_number=columns_entry.get()
        if not lines_number.isdigit() or not columns_number.isdigit():
            show_error("行和列必须是整数")
            return
        else:
            lines_number=int(lines_number)
            columns_number=int(columns_number)
            choose_seats_numbers_surface.destroy()
            return
    
    confirm_button=Button(choose_seats_numbers_surface,text="确定",
                        command=get_seats_number,font=("",12))
    confirm_button.pack(fill="both")

    choose_seats_numbers_surface.mainloop()
    return

# 选择“空”座位
def choose_blank_seats():
    global seats,lines_number,columns_number

    choose_blank_seats_surface=pygame.display.set_mode((100+45*columns_number,200+45*(lines_number-1)))
    pygame.display.set_caption("选择空座位")

    # 确认按钮
    confirm_button_block=pygame.Rect(50+45*columns_number/2-50,100+45*lines_number,100,40)
    confirm_button_word=LITTLE_FONT.render("确 认",True,WHITE)
    confirm_button_word_rect=confirm_button_word.get_rect()
    confirm_button_word_rect.center=(50+45*columns_number/2,120+45*lines_number)

    """讲台在屏幕下方，窗户在屏幕右侧"""
    # 讲台
    stage_block=pygame.Rect(45*columns_number-40,50+45*lines_number,85,30)
    stage_word=VERY_LITTLE_FONT.render("讲台",True,WHITE)
    stage_word_rect=stage_word.get_rect()
    stage_word_rect.center=(2.5+45*columns_number,65+45*lines_number)
    # 座位
    seats_blocks_rect=[[pygame.Rect(50+45*i,50+45*j,40,40)
             for j in range(lines_number)] for i in range(columns_number)]
    seats_blocks_buf=[[False for j in range(lines_number)]
             for i in range(columns_number)]
    # buf 用来临时存储是否设置成了 blank, False 为不是 blank
    seats_blocks_color=[[DARK_GRAY for j in range(lines_number)]
             for i in range(columns_number)]

    # 综合 buf 与 color 判断 block 的颜色
    def get_block_color(x,y):
        if seats_blocks_buf[x][y]==True:
            return YELLOW
        else:
            return seats_blocks_color[x][y]

    while True:

        choose_blank_seats_surface.fill(GRAY)
        pygame.draw.rect(choose_blank_seats_surface,DARK_GRAY,stage_block)
        choose_blank_seats_surface.blit(stage_word,stage_word_rect)
        pygame.draw.rect(choose_blank_seats_surface,DARK_GRAY,confirm_button_block)
        choose_blank_seats_surface.blit(confirm_button_word,confirm_button_word_rect)
        for x in range(columns_number):
            for y in range(lines_number):
                pygame.draw.rect(choose_blank_seats_surface,
                get_block_color(x,y),seats_blocks_rect[x][y])
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)

            # 鼠标悬停
            mouse_pos=pygame.mouse.get_pos()
            if IN(mouse_pos,confirm_button_block.topleft,confirm_button_block.bottomright):
                confirm_button_word=LITTLE_FONT.render("确 认",True,YELLOW)
            else:
                confirm_button_word=LITTLE_FONT.render("确 认",True,WHITE)
                for x in range(columns_number):
                    for y in range(lines_number):
                        if IN(mouse_pos,seats_blocks_rect[x][y].topleft,
                                seats_blocks_rect[x][y].bottomright):
                            seats_blocks_color[x][y]=YELLOW
                            break
                        else:
                            seats_blocks_color[x][y]=DARK_GRAY
            
            # 鼠标点击
            if event.type==MOUSEBUTTONUP:
                # 点击确认按钮
                if IN(mouse_pos,confirm_button_block.topleft,confirm_button_block.bottomright):
                    for x in range(columns_number):
                        for y in range(lines_number):
                            seats[y][x]="BLANK" if seats_blocks_buf[x][y] else ""
                    pygame.display.quit()
                    return
                
                # 点击座位
                elif IN(mouse_pos,seats_blocks_rect[0][0].topleft,
                    seats_blocks_rect[-1][-1].bottomright):
                    for x in range(columns_number):
                        for y in range(lines_number):
                            if IN(mouse_pos,seats_blocks_rect[x][y].topleft,
                                    seats_blocks_rect[x][y].bottomright):
                                seats_blocks_buf[x][y]=not seats_blocks_buf[x][y]
                                break
                            else:
                                pass
        
        pygame.display.update()
    return

# 设置轮换规则
def set_change_mode():
    global seats
    change_cnt=0
    
    set_change_mode_surface=pygame.display.set_mode((140+70*columns_number,170+35*lines_number))
    pygame.display.set_caption("设置轮换规则")
    
    """讲台在屏幕下方，窗户在屏幕右侧"""
    # 轮换前
    pre_reminder_word=VERY_LITTLE_FONT.render("轮换前",True,WHITE)
    pre_reminder_word_rect=pre_reminder_word.get_rect()
    pre_reminder_word_rect.center=(40,20)
    # 讲台
    pre_stage_block=pygame.Rect(35*columns_number-30,40+35*lines_number,65,30)
    pre_stage_word=VERY_LITTLE_FONT.render("讲台",True,WHITE)
    pre_stage_word_rect=pre_stage_word.get_rect()
    pre_stage_word_rect.center=(35*columns_number,55+35*lines_number)
    # 座位
    pre_seats_blocks_rect=[[pygame.Rect(40+35*i,40+35*j,30,30)
             for j in range(lines_number)] for i in range(columns_number)]
    
    # 轮换后
    pst_reminder_word=VERY_LITTLE_FONT.render("轮换后",True,WHITE)
    pst_reminder_word_rect=pst_reminder_word.get_rect()
    pst_reminder_word_rect.center=(110+35*columns_number,20)
    # 讲台
    pst_stage_block=pygame.Rect(40+70*columns_number,40+35*lines_number,65,30)
    pst_stage_word=VERY_LITTLE_FONT.render("讲台",True,WHITE)
    pst_stage_word_rect=pst_stage_word.get_rect()
    pst_stage_word_rect.center=(70+70*columns_number,55+35*lines_number)
    # 座位
    pst_seats_blocks_rect=[[pygame.Rect(110+35*(columns_number+i),40+35*j,30,30)
             for j in range(lines_number)] for i in range(columns_number)]

    while True:
        set_change_mode_surface.fill(GRAY)

        # 轮换前
        set_change_mode_surface.blit(pre_reminder_word,pre_reminder_word_rect)
        pygame.draw.rect(set_change_mode_surface,DARK_GRAY,pre_stage_block)
        set_change_mode_surface.blit(pre_stage_word,pre_stage_word_rect)
        for x in range(columns_number):
            for y in range(lines_number):
                if seats[y][x]=="BLANK":
                    continue
                pygame.draw.rect(set_change_mode_surface,DARK_GRAY,
                        pre_seats_blocks_rect[x][y])

        # 分割线
        pygame.draw.line(set_change_mode_surface,DARK_GRAY,
            (70+35*columns_number,10),(70+35*columns_number,70+35*lines_number))

        # 轮换后
        set_change_mode_surface.blit(pst_reminder_word,pst_reminder_word_rect)
        pygame.draw.rect(set_change_mode_surface,DARK_GRAY,pst_stage_block)
        set_change_mode_surface.blit(pst_stage_word,pst_stage_word_rect)
        for x in range(columns_number):
            for y in range(lines_number):
                if seats[y][x]=="BLANK":
                    continue
                pygame.draw.rect(set_change_mode_surface,DARK_GRAY,
                        pst_seats_blocks_rect[x][y])

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.display.quit()
                _exit(0)

        pygame.display.update()
    return

"""WARNING: UNCOMPLETED"""
def main():
    global data_file_name,seats

    # greet()
    # sleep(0.2)
    mode=import_or_create()
    if mode=="import":
        data_file_name=select_file([("数据文件","*.rsd")]) # ".rsd" 取自 random、seat、data 首字母

    elif mode=="new":
        choose_seats_numbers()
        # print(lines_number,columns_number)
        seats=[["" for y in range(columns_number)] for x in range(lines_number)]
         # seats[x][y]: x为行号，y为列号，后门处为[0][0]
        choose_blank_seats()
        print(seats)
        set_change_mode()

    elif mode=="last":
        pass

if __name__=='__main__':
    main()