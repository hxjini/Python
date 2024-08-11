#키보드로 그리기
import turtle as t
t.shape('turtle')
import keyboard
while True:
  if keyboard.is_pressed('left'):
    t.left(10)
  elif keyboard.is_pressed('right'):
    t.right(10)
  elif keyboard.is_pressed('up'):
    t.forward(10)
  elif keyboard.is_pressed('down'):
    t.backward(10)
  elif keyboard.is_pressed('a'):
    print('quit')
  quit()
  break