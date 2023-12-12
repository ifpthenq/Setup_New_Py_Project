###############################
#   This program sets up a new project

import os
import sys
import time
import logging
import shutil
from lib import logs
from lib.ahConfig import ahConfig
import shutil

log = logging.getLogger('lib.logs.' + __name__)
log.info("==== INITIATE LOGFILE ====")

# Step 1: Create a new project folder

def create_project_directory(directory, scripts_path):
    log.info("DBG: create_project_directory")
    full_path = os.path.join(scripts_path, directory)
    if not os.path.exists(full_path):
        print('Creating project ' + full_path)
        os.makedirs(full_path)

    # Step 2: Copy create_venv.bat to the project folder
    create_venv_path = os.path.join(full_path, 'create_venv.bat')
    log.info("Copying create_venv.bat to " + create_venv_path)
    shutil.copy('create_venv.bat', full_path)
    log.info("Copy completed")

    # Step 3: Copy lib directory to project folder
    lib_path = os.path.join(full_path, 'lib')
    log.info("Copying lib directory to " + lib_path)
    shutil.copytree('lib', lib_path)
    log.info("Copy completed")

    # Step 4: Copy config.txt to project folder
    config_path = os.path.join(full_path, 'config.txt')
    log.info("Copying config.txt to " + config_path)
    shutil.copy('config.txt', full_path)
    log.info("Copy completed")

    # Step 5: Create main.py in project folder
    main_path = os.path.join(full_path, 'main.py')
    log.info("Creating main.py in " + main_path)
    main_file = open(main_path, 'w')
    main_file.write('import os\n')
    main_file.write('import sys\n')
    main_file.write('import time\n')
    main_file.write('import logging\n')
    main_file.write('from lib import logs\n')
    main_file.write('from lib.ahConfig import ahConfig\n')
    main_file.write('\n')
    main_file.write('log = logging.getLogger(\'lib.logs.\' + __name__)\n')
    main_file.write('log.info("==== INITIATE LOGFILE ====")\n')
    main_file.write('\n')
    main_file.write('if __name__ == \'__main__\':\n')
    main_file.write('    log.info("BEGGINING MAIN")\n')
    main_file.write('\n')
    main_file.write('    config = ahConfig()\n')
    main_file.write('    cfg = config.get_config_section(\'config\')\n')
    main_file.write('    project_name = cfg[\'project_name\']\n')
    main_file.close()
    log.info("main.py created")

    # Step 6: Copy gitignit.bat to project folder
    git_path = os.path.join(full_path, 'gitinit.bat')
    log.info("Copying gitinit.bat to " + git_path)
    shutil.copy('gitinit.bat', full_path)
    log.info("Copy completed")

    # Step 7: Create gitignore.txt in project folder
    gitignore_path = os.path.join(full_path, '.gitignore')
    log.info("Creating .gitignore in " + gitignore_path)
    gitignore_file = open(gitignore_path, 'w')
    gitignore_file.write('*.pyc\n')
    gitignore_file.write('*.log\n')
    gitignore_file.write('*.txt\n')
    gitignore_file.write('notes')
    gitignore_file.close()
    log.info(".gitignore created")

    # Step 8: Copy launchCMD.bat to project folder
    launchCMD_path = os.path.join(full_path, 'launchCMD.bat')
    log.info("Copying launchCMD.bat to " + launchCMD_path)
    shutil.copy('launchCMD.bat', full_path)
    log.info("Copy completed")
    
    

if __name__ == '__main__':
    log.info("BEGGINING MAIN")

    config = ahConfig()
    cfg = config.get_config_section('config')
    project_name = cfg['project_name']
    scripts_path = cfg['scripts_path']
    createDirectory = create_project_directory(project_name, scripts_path)
