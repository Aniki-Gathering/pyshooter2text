from configobj import ConfigObj

config = ConfigObj("setup.ini",encoding='UTF8')
s1=config['keyboard_shortcut']['screenshot']
s2=config['keyboard_shortcut']['minimodel']
s3=config['background']['path']
s4=config['setting']['minimize']
s5=config['setting']['welcome']
config['keyboard_shortcut']['screenshot'] ='control+r'
config['keyboard_shortcut']['minimodel']= 'control+t'
config.write()