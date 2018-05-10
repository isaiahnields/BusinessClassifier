import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from scraper import facebook, google, yelp
from iohandler import *


class Application(tk.Frame):

    def __init__(self, master=None):
        # passes the tk root to the tk frame object
        super().__init__(master)

        # packs the the frame inside of the root application
        self.pack()

        # initializes tkinter variables
        self.data_location_variable = tk.StringVar()
        self.results_location_variable = tk.StringVar()
        self.name_rows = tk.StringVar()
        self.location_rows = tk.StringVar()
        self.facebook_access_token = tk.StringVar()
        self.geonames_username = tk.StringVar()
        self.yelp_api_key = tk.StringVar()
        self.facebook_variable = tk.IntVar()
        self.google_variable = tk.IntVar()
        self.yelp_variable = tk.IntVar()

        # restores the variables to their value stored in data
        self.restore_variables()

        # packs frames into root window
        self.create_file_frame().grid(row=0, column=0, pady=10)
        self.create_options_frame().grid(row=1, column=0, sticky='w', pady=10)
        tk.Button(self, text="Run", width=5).grid(row=2, column=0, sticky='e')

    def restore_variables(self):
        """
        Initializes variables that are necessary for the Tkinter graphical user interface.
        """

        # loads the location and key variables from data
        file_locations = open("data/locations.txt", 'r').read().split('\n')
        keys = open("data/keys.txt", 'r').read().split('\n')

        # sets the tkinter variables to the values pulled from data
        self.data_location_variable.set(file_locations[0])
        self.results_location_variable.set(file_locations[1])
        self.facebook_access_token.set(keys[0])
        self.geonames_username.set(keys[1])
        self.yelp_api_key.set(keys[2])

        # set the Google option to true as it doesn't need an API key

        self.google_variable.set(True)

        # if the Facebook key is not empty and the GeoNames username is not empty
        if keys[0] != "" and keys[0] != "":

            # check the option to scrape Facebook
            self.facebook_variable.set(True)

        # if the Yelp key is not empty
        if keys[2] != "":

            # check the option to scrape Yelp
            self.yelp_variable.set(True)

        # adds traces to variables so that they are saved when edited
        self.data_location_variable.trace("w", self.save)
        self.results_location_variable.trace("w", self.save)
        self.facebook_access_token.trace("w", self.save)
        self.geonames_username.trace("w", self.save)
        self.yelp_api_key.trace("w", self.save)
        self.facebook_variable.trace("w", self.save)
        self.google_variable.trace("w", self.save)
        self.yelp_variable.trace("w", self.save)

    def create_file_frame(self):
        """
        Returns a frame that contains all the widgets necessary for choosing how business data is read and saved.

        :return file_frame: the frame used for choosing how business data is read and saved
        """

        # creates the file frame
        file_frame = tk.Frame(master=self)

        # creates and grids widgets necessary for loading data file
        tk.Label(file_frame, text="Data file", width=10, anchor='w').grid(row=0, column=0)
        tk.Entry(file_frame, width=35, textvariable=self.data_location_variable).grid(row=0, column=1)
        tk.Button(file_frame, width=5, text="...", command=self.choose_data_file).grid(row=0, column=2)

        # creates and grids widgets necessary for choosing results file
        tk.Label(file_frame, text="Results file", width=10, anchor='w').grid(row=1, column=0, sticky='w')
        tk.Entry(file_frame, width=35, textvariable=self.results_location_variable).grid(row=1, column=1)
        tk.Button(file_frame, width=5, text="...", command=self.choose_results_location).grid(row=1, column=2)

        return file_frame

    def create_options_frame(self):
        """
        Creates a frame that contains the widgets necessary for choosing which services are used and specifying api
        keys.

        :return options_frame: the frame used for choosing which services are used and specifying api keys
        """

        # creates the options frame
        options_frame = tk.Frame(master=self)

        # adds Facebook label and check box to the options frame
        tk.Label(options_frame, text="Facebook", anchor='w').grid(row=1, column=0)
        tk.Checkbutton(options_frame, variable=self.facebook_variable).grid(row=1, column=1)

        # adds Google label and check box to the options frame
        tk.Label(options_frame, text="Google", anchor='w').grid(row=2, column=0)
        tk.Checkbutton(options_frame, variable=self.google_variable).grid(row=2, column=1)

        # adds Yelp label and check box to the options frame
        tk.Label(options_frame, text="Yelp", anchor='w').grid(row=3, column=0)
        tk.Checkbutton(options_frame, variable=self.yelp_variable).grid(row=3, column=1)

        # adds Facebook access token label and entry box to the options frame
        tk.Label(options_frame, text="Facebook Access Token", anchor='w').grid(row=1, column=2)
        tk.Entry(options_frame, width=20, textvariable=self.facebook_access_token).grid(row=1, column=3)

        # adds GeoNames username label and entry box to the options frame
        tk.Label(options_frame, text="GeoNames Username", anchor='w').grid(row=2, column=2)
        tk.Entry(options_frame, width=20, textvariable=self.geonames_username).grid(row=2, column=3)

        # adds Yelp api key label and entry box to the options frame
        tk.Label(options_frame, text="Yelp API Key", anchor='w').grid(row=3, column=2)
        tk.Entry(options_frame, width=20, textvariable=self.yelp_api_key).grid(row=3, column=3)

        return options_frame

    def choose_data_file(self):
        """
        Prompts the user to choose the location of the data file.
        """

        # prompts the user for the file location
        file_location = askopenfilename(defaultextension='.csv')

        # sets the data location variable to the chosen file location
        self.data_location_variable.set(file_location)

    def choose_results_location(self):
        """
        Prompts the user to choose the location where the results file should be saved.
        """

        # prompts the user for the file location
        file_location = asksaveasfilename(defaultextension='.csv', filetypes=[('CSV', '.csv')])

        # sets the data location variable to the chosen file location
        self.results_location_variable.set(file_location)

    def save(self, *args):
        """
        Saves the keys and locations entered by the user.
        """

        # opens the keys file
        keys_file = open('data/keys.txt', 'w')

        # writes the keys to keys file
        keys_file.write(self.facebook_access_token.get() + '\n')
        keys_file.write(self.geonames_username.get() + '\n')
        keys_file.write(self.yelp_api_key.get() + '\n')

        # opens the file location file
        location_file = open('data/locations.txt', 'w')

        # writes the locations to the locations file
        location_file.write(self.data_location_variable.get() + '\n')
        location_file.write(self.results_location_variable.get() + '\n')

    def run(self):
        """
        Runs the Business classification algorithm based on the user settings.
        """

        # loads instances of scrapers
        self.facebook = facebook.Facebook(self.facebook_access_token.get(), self.geonames_username.get())
        self.google = google.Google()
        self.yelp = yelp.Yelp(self.yelp_api_key.get())

# creates the tkinter root
root = tk.Tk()

# changes the title of the window to business classifier
root.title('Business Classifier')

# change the size of the main window
root.geometry('500x220')

# disallow the main window from being resized
root.resizable(False, False)

# creates the the application and starts the loop
app = Application(master=root)
app.mainloop()
