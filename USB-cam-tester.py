import wmi,cv2

def camfunction(): 
  vid = cv2.VideoCapture(1, cv2.CAP_DSHOW)
  vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  vid.set(cv2.CAP_PROP_FOURCC, 0x32595559)
  vid.set(cv2.CAP_PROP_FPS, 25)
  while(True):
    try:
      ret, frame = vid.read()
      cv2.imshow('Webcam window: Press / or disconnect USB to close window.', frame)
      # desired button of your choice
      if cv2.waitKey(1) & 0xFF == ord('/'):
        break
    except:
      break
  vid.release()
  cv2.destroyAllWindows()


raw_wql = "SELECT * FROM __InstanceCreationEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
c = wmi.WMI()
watcher = c.watch_for(raw_wql=raw_wql)

while 1:
  usb = watcher()
  camfunction()
