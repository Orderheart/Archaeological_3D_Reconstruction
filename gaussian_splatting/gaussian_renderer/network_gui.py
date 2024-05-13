#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use 
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

import torch
import traceback  #处理和跟踪异常
import socket #网络编程
import json
from scene.cameras import MiniCam #自定义类

host = "127.0.0.1" #主机地址
port = 6009  #端口号

conn = None #连接对象
addr = None #地址

#创建一个新的IPv4 TCP套接字，并将其赋值给listener。这个listener套接字可以被用来监听和接受网络连接。
#socket.AF_INET:地址族的类型，AF_INET表示IPv4的网络通信协议（127.0.0.1）
#socket.SOCK_STREAM:流套接字类型，可靠的、双向、基于链接的字节流，是创建TCP链接的套接字类型
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


#初始化网络监听器
def init(wish_host, wish_port):
    #函数内部改变全局变量的值，你需要使用global关键字
    global host, port, listener
    host = wish_host
    port = wish_port
    #绑定listener到host和port里
    listener.bind((host, port))
    listener.listen()
    listener.settimeout(0)

def try_connect():
    global conn, addr, listener
    try:
        #调用listener套接字的accept方法来接受一个新的网络连接
        conn, addr = listener.accept()
        print(f"\nConnected by {addr}")
        #这行代码设置conn套接字的超时时间为无限。在网络编程中，超时是一个重要的概念。当你尝试接收数据但是没有数据到达时，程序可能会阻塞在那里等待。
        #通过设置超时时间，你可以让程序在等待了一定时间后继续执行，而不是永远地等待。
        #这里设置的超时时间为无限，意味着如果没有数据到达，conn套接字的接收操作会一直等待，直到有数据到达。
        conn.settimeout(None)
    except Exception as inst:
        pass
            
def read():
    global conn
    #从conn连接中接收4个字节的数据,这4个字节的数据通常被用来表示接下来要接收的消息的长度。
    messageLength = conn.recv(4)
    #将接收到的4个字节的数据（这是一个字节字符串）转换为一个整数，这个整数表示接下来要接收的消息的长度.'little'表示使用小端字节序来解码
    messageLength = int.from_bytes(messageLength, 'little')
    #从conn连接中接收messageLength个字节的数据，并将其赋值给message。这些数据就是实际的消息内容。
    message = conn.recv(messageLength)
    return json.loads(message.decode("utf-8"))

def send(message_bytes, verify):
    global conn
    if message_bytes != None:
        conn.sendall(message_bytes)
    #计算verify字符串的长度，然后将这个长度转换为一个4字节的字节字符串，并将其发送出去。
    conn.sendall(len(verify).to_bytes(4, 'little'))
    #将verify字符串转换为一个字节字符串，并将其发送出去
    conn.sendall(bytes(verify, 'ascii'))

def receive():
    message = read()

    #这两行代码从消息中提取图像的宽度和高度
    width = message["resolution_x"]
    height = message["resolution_y"]

    if width != 0 and height != 0:
        try:
            #训练标志
            do_training = bool(message["train"])
            #获得垂直方向的值和水平方向的值
            fovy = message["fov_y"]
            fovx = message["fov_x"]
            #获得近裁剪平面和远裁剪平面。-> 计算投影矩阵
            znear = message["z_near"]
            zfar = message["z_far"]

            do_shs_python = bool(message["shs_python"])
            do_rot_scale_python = bool(message["rot_scale_python"])
            #bool，标志是否保持连接
            keep_alive = bool(message["keep_alive"])
            #用于缩放操作的修饰值
            scaling_modifier = message["scaling_modifier"]
            #获取"view_matrix"字段的值，将其转换为一个PyTorch张量，然后将其形状重塑为4x4的矩阵，并将其移动到CUDA设备上。
            #这可能是一个世界视图变换矩阵。
            world_view_transform = torch.reshape(torch.tensor(message["view_matrix"]), (4, 4)).cuda()
            #这两行将世界视图变换矩阵的第二列和第三列的符号取反。这可能是一个必要的坐标系转换。
            world_view_transform[:,1] = -world_view_transform[:,1]
            world_view_transform[:,2] = -world_view_transform[:,2]
            #获取"view_projection_matrix"字段的值，将其转换为一个PyTorch张量，然后将其形状重塑为4x4的矩阵，并将其移动到CUDA设备上。
            #这可能是一个全投影变换矩阵。
            full_proj_transform = torch.reshape(torch.tensor(message["view_projection_matrix"]), (4, 4)).cuda()
            full_proj_transform[:,1] = -full_proj_transform[:,1]
            #这行使用之前从消息中提取的参数创建一个MiniCam对象。MiniCam是scene是一个自定义的类，用于处理图像和机器学习任务。
            custom_cam = MiniCam(width, height, fovy, fovx, znear, zfar, world_view_transform, full_proj_transform)
        except Exception as e:
            print("")
            traceback.print_exc()
            raise e
        return custom_cam, do_training, do_shs_python, do_rot_scale_python, keep_alive, scaling_modifier
    #如果高度和宽度都是0，那么函数返回一堆None值
    else:
        return None, None, None, None, None, None

    
