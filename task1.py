def define(name,**kwargs):
  print(name)
  for key, value in kwargs.items():
    print("{} - {}".format(key,value))

define(name='Japan', population='126 million', language='Japanese')
