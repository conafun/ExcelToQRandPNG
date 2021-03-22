import turtle as tl
def main(n):
	m = 5 
	for i in range(18):
		for j in range(36):
			tl.forward(m)  #向前画线
			tl.right(10)   #向右转60°
		tl.right(20)
		
	tl.exitonclick()  #点击画面退出
 
 
if __name__ == '__main__':
	main(5)  
