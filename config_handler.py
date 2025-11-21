"""

Options Module: Will handle anything related to
Change or Edit Options inside converter_config.config file

Copyright (C) 2024 DooMMetaL

"""

import os
from PyQt6.QtWidgets import QMessageBox, QFileDialog

class ConfigurationHandler:
    def __init__(self, option_file: str) -> None:
        """
        Handle the main Configuration Options for the tool:\n
        Loads Configuration at start of the tool, write new data into it, selection of folders.
        """
        self.self = ConfigurationHandler
        self.option_file = option_file
        self.option_dict: dict = {'First_Run': 'False', 'SizeX': '', 'SizeY': '', 'SC_Folder': '', 'Deploy_Folder': ''}
        self.__load_configuration_file()
    
    def __load_configuration_file(self) -> None:
        """
        Load Configurations from Manager.config file\n
        If for some reason this Config file don't exists will create a new one\n
        :Params: self.option_file STR which is the path to the configuration file\n
        read_write_options() -> Dictionary which contains Configuration data
        """
        
        database_from_string_to_list: list[str] = []
        
        try:
            with open(self.option_file, 'rt') as read_config:
                read_lines_config: list[str] = read_config.readlines()
                for config_line in read_lines_config:
                    database_from_string_to_list.append(config_line)
        except FileNotFoundError:
            """If something bad happens, this will write an 'emergency config file', just in case that this files don't exist"""
            QMessageBox.critical(None, f'CRITICAL ERROR!', f'Couldn\'t find Configuration file!\nin: {self.option_file}\nWill create a new one, please restart the Tool', QMessageBox.StandardButton.Ok)
            emergency_dict = {'First_Run': 'True', 'SizeX': '640', 'SizeY': '360', 'SC_Folder': 'None', 'Deploy_Folder': 'None'}
            ConfigurationHandler.write_config_file(config_file_path=self.option_file, configuration_dict=emergency_dict)
            exit()
        
        header_type_complete_string = database_from_string_to_list[0] # Loading this just in case that anytime will came usable
        first_run_flag_complete_string = database_from_string_to_list[1].split('=')
        resolution_x_complete_string = database_from_string_to_list[2].split('=')
        resolution_y_complete_string = database_from_string_to_list[3].split('=')
        severed_chains_folder_complete_string = database_from_string_to_list[4].split('=')
        deploy_folder_complete_string = database_from_string_to_list[5].split('=')
        
        first_run_flag = first_run_flag_complete_string[1].replace(' ', '').replace('\n','')
        resolution_x = resolution_x_complete_string[1].replace(' ', '').replace('\n','')
        resolution_y = resolution_y_complete_string[1].replace(' ', '').replace('\n','')
        severed_chains_folder = severed_chains_folder_complete_string[1].strip().replace('\n','').replace('/', '/')
        deploy_folder = deploy_folder_complete_string[1].strip().replace('\n','').replace('/', '/')

        if (first_run_flag == 'True') or (first_run_flag == ''):
            QMessageBox.information(None, 'FIRST START-UP', 'We will do a start-up configuration\nplease follow the steps', QMessageBox.StandardButton.Ok)
            self.option_dict['First_Run'] = 'False'
        
        if resolution_x.isdigit():
            self.option_dict['SizeX'] = resolution_x
        else:
            self.option_dict['SizeX'] = '1280'

        if resolution_y.isdigit():
            self.option_dict['SizeY'] = resolution_y
        else:
            self.option_dict['SizeY'] = '720'
        
        if severed_chains_folder and severed_chains_folder != 'None':
            self.option_dict['SC_Folder'] = severed_chains_folder
        else:
            severed_chains_files_path = ConfigurationHandler.select_sc_folder()
            self.option_dict['SC_Folder'] = severed_chains_files_path
            
        if deploy_folder and deploy_folder != 'None':
            self.option_dict['Deploy_Folder'] = deploy_folder
        else:
            indicate_deploy_folder = ConfigurationHandler.select_deploy_folder()
            self.option_dict['Deploy_Folder'] = indicate_deploy_folder

        ConfigurationHandler.write_config_file(config_file_path=self.option_file, configuration_dict=self.option_dict)
        self.option_dict = self.option_dict

    @staticmethod
    def write_config_file(config_file_path: str, configuration_dict: dict) -> None:
        """
        Write into the configuration file which is read from the Option Dict\n
        :params: config_file_path [Path to Configuration File], configuration_dict [Dictionary containing the Configuration Data]\n
        write_options() -> None
        """
        with open(config_file_path, 'w') as writing_options:
            header = f'[CONFIG]\n'
            firstrun_flag = f"FIRST_RUN = {configuration_dict.get(f'First_Run')}\n"
            res_x = f"DEFAULT_RES_X = {configuration_dict.get(f'SizeX')}\n"
            res_y = f"DEFAULT_RES_Y = {configuration_dict.get(f'SizeY')}\n"
            sc_folder = f"SC_FOLDER = {configuration_dict.get(f'SC_Folder')}\n"
            deploy_folder = f"DEPLOY_FOLDER = {configuration_dict.get(f'Deploy_Folder')}"
            grabbing_every_str = f'{header}{firstrun_flag}{res_x}{res_y}{sc_folder}{deploy_folder}'
            writing_options.write(grabbing_every_str)
            writing_options.close()
    
    @staticmethod
    def try_again_select_folder() -> str:
        """
        Try Again selecting the Severed Chains 'files' Folder, until user get it
        try_again_select_folder() -> get_folder ; path to 'files' Folder
        """
        get_folder: str = f''
        try_again_dialog = QMessageBox.warning(None, f'Cannot find SC FOLDER', f'Please select the path to the \"files\" folder inside Severed Chains Folder', QMessageBox.StandardButton.Ok)
        get_folder = QFileDialog.getExistingDirectory(None, f'Please select the folder called \"files\" inside SC root folder')
        return get_folder
    
    @staticmethod
    def select_sc_folder() -> str:
        """
        Select Severed Chains Folder:\n
        This function selects Severed Chains Folder while checking it's the correct folder.\n
        Loop will not end until the correct conditions are met, a little risky since is a While True, but more elegant.        
        """
        final_sc_path: str = ''
        while True:
            QMessageBox().information(None, f'SELECT SC FILES FOLDER', f'Please select the folder called \"files\" inside SC root folder', QMessageBox.StandardButton.Ok)
            sc_folder_path = QFileDialog.getExistingDirectory(None, f'SELECT SC FILES FOLDER')

            # If the user cancelled the dialog, return empty path
            # Which will kill the loop & close the selection process.
            if not sc_folder_path:
                return ''

            sc_folder_check_1: bool = os.path.exists(f'{sc_folder_path}/SECT')
            sc_folder_check_2: bool = os.path.exists(f'{sc_folder_path}/characters')
            sc_folder_check_3: bool = os.path.exists(f'{sc_folder_path}/monsters')
            if sc_folder_check_1 and sc_folder_check_2 and sc_folder_check_3:
                final_sc_path = sc_folder_path
                break
        return final_sc_path
    
    @staticmethod
    def select_deploy_folder() -> str:
        """
        Select Deploy Folder:\n
        Select a folder to deploy the converted files.\n
        We strongly recommend to do not use the Severed Chains Folder. However it's possible.
        """
        indicate_deploy_folder: str = f''
        title_wn: str = f'SELECT A FOLDER TO DEPLOY'
        recommend: str = f'Please, select a folder to deploy converted files.\nRecommended: Do not create inside SC FOLDER'
        QMessageBox.information(None, title_wn, recommend, QMessageBox.StandardButton.Ok)
        indicate_deploy_folder = QFileDialog.getExistingDirectory(None, f'SELECT A FOLDER TO DEPLOY FILES')

        # If the user cancelled the dialog, return empty path
        # Which will kill the loop & close the selection process.
        if not indicate_deploy_folder:
                return ''

        return indicate_deploy_folder
    
    def get_sc_folder(self) -> str:
        # Return the stored SC_Folder value as a string (fallback to empty string)
        self.sc_folder = str(self.option_dict.get('SC_Folder', ''))
        return self.sc_folder
