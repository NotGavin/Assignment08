#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# GChan, 2020-Mar-15, created file
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODO Add Code to the CD class
    def __init__(self, idno, ttl, art):
        # -- ATTRIBUTES -- #
        self.__idno = idno
        self.__ttl = ttl
        self.__art = art
         
    @property
    def idno(self):
        return self.__idno
    
    @idno.setter
    def idno(self, idnum):
        if idnum.isnumeric():
            self.__position = int(idnum)
        else:
            raise Exception("ID should be a number")
    
    @property
    def ttl(self):
        return self.ttl
    
    @ttl.setter
    def ttl(self, title):
        if title.isnumeric():
            raise Exception("Title should be a string")
        else:
            self.__ttl = title
            
    @property
    def art(self):
        return self.art
    
    @art.setter
    def art(self, artist):
        if artist.isnumeric():
            raise Exception("Artist name should be a string")
        else:
            self.__art = artist    

    def organize(self):
        return '{}\t\t{} by: {}'.format(self.__idno, self.__ttl, self.__art)
    def __str__(self):
        return self.organize()
    def organizeSave(self):
        return '{}\t\t{} by: {}\n'.format(self.__idno, self.ttl, self.__art)

    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file
    def read_file(file_name, lst_Inventory):
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            cd = CD(int(data[0]),data[1],data[2])
            lst_Inventory.append(cd)
        objFile.close()        
    # TODO Add code to process data to a file
    def write_file(file_name, table):
        objFile = open(file_name, 'w')
        for cd in table:
            objFile.write(cd.organizeSave())
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    # TODO add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')    
    # TODO add code to captures user's 
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODO add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for CD in table:
            print(CD)
        print('======================================')
    # TODO add code to get CD data from user
    @staticmethod
    def input_CDinfo():
        """Gets CD information as input from user
        
        Args:
            none
            
        Returns:
            intID, StrTitle, strArtist
        
        """
        intID = int(input('Enter ID: ').strip())
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return intID, strTitle, strArtist

# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
while True:
    # show user current inventory
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # let user exit program
    if strChoice == 'x':
        break
            
    # let user add data to the inventory
    elif strChoice == 'a':
        nID, nTitle, nArtist = IO.input_CDinfo()
        newCD = CD(nID, nTitle, nArtist)
        lstOfCDObjects.append(newCD)
        IO.show_inventory(lstOfCDObjects)
        continue  
    
    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  
    
    # let user load inventory from file
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = []
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
            continue 


