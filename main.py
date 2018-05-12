import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from scraper import facebook, google, yelp
from iohandler import reader, writer
from tkinter import messagebox
import webbrowser


class Application(tk.Frame):

    def __init__(self, master=None):

        # passes the tk root to the tk frame object
        super().__init__(master)

        # packs the the frame inside of the root application
        self.pack()

        # initializes tkinter variables
        self.data_location_variable = tk.StringVar()
        self.results_location_variable = tk.StringVar()
        self.name_columns = tk.StringVar()
        self.location_columns = tk.StringVar()
        self.facebook_access_token = tk.StringVar()
        self.geonames_username = tk.StringVar()
        self.yelp_api_key = tk.StringVar()

        # restores the variables to their value stored in data
        self.restore_variables()

        # packs frames into root window
        self.create_file_frame().grid(row=0, column=0, pady=10)
        self.create_columns_frame().grid(row=1, column=0)
        self.create_options_frame().grid(row=2, column=0, pady=10)

        tk.Button(self, text="Run", width=5, command= self.run).grid(row=3, column=0, sticky='e')

    def restore_variables(self):
        """
        Initializes variables that are necessary for the Tkinter graphical user interface.
        """

        # attempts to load in the data from storage and, if no file is present, one is created
        try:

            # opens the file that stores the location of the csv files
            file_locations = open("data/locations.txt", 'r+').read().split('\n')

            # loads that data into their proper Tkinter variables
            self.data_location_variable.set(file_locations[0])
            self.results_location_variable.set(file_locations[1])

        except FileNotFoundError:

            # if the file could not be found, create a new one
            open("data/locations.txt", 'w+')

        except IndexError:

            # if the file could not be found, create a new one
            open("data/columns.txt", 'w+')

        try:

            # opens the data file with the columns of interest in it
            columns = open("data/columns.txt", 'r+').read().split('\n')

            # loads the column data into the proper Tkinter variables
            self.name_columns.set(columns[0])
            self.location_columns.set(columns[1])

        except FileNotFoundError:

            # if the file could not be found, create a new one
            open("data/columns.txt", 'w+')

        except IndexError:

            # if the file could not be found, create a new one
            open("data/columns.txt", 'w+')

        try:

            # opens the keys file and reads the data
            keys = open("data/keys.txt", 'r+').read().split('\n')

            # reads the data into the proper Tkinter variables
            self.facebook_access_token.set(keys[0])
            self.geonames_username.set(keys[1])
            self.yelp_api_key.set(keys[2])

        except FileNotFoundError:

            # if the file could not be found, create a new one
            open("data/keys.txt", 'w+')

        except IndexError:

            # if the file could not be found, create a new one
            open("data/columns.txt", 'w+')

        # adds traces to variables so that they are saved when edited
        self.data_location_variable.trace("w", self.save)
        self.results_location_variable.trace("w", self.save)
        self.name_columns.trace("w", self.save)
        self.location_columns.trace("w", self.save)
        self.facebook_access_token.trace("w", self.save)
        self.geonames_username.trace("w", self.save)
        self.yelp_api_key.trace("w", self.save)

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
        tk.Label(file_frame, text="Results file", width=10, anchor='w').grid(row=1, column=0)
        tk.Entry(file_frame, width=35, textvariable=self.results_location_variable).grid(row=1, column=1)
        tk.Button(file_frame, width=5, text="...", command=self.choose_results_location).grid(row=1, column=2)

        return file_frame

    def create_columns_frame(self):
        """
        Returns a frame that contains the widgets necessary for chooseing which columns contain business data.

        :return columns_frame: a frame containing the widgets for choosing the columns of the csv document
        """

        # creates the columns frame
        columns_frame = tk.Frame(master=self)

        # creates and grids widgets necessary for choosing which columns in the file correspond to which business data
        tk.Label(columns_frame, text="Business Name Columns", width=20, anchor='w').grid(row=0, column=0)
        tk.Entry(columns_frame, width=30, textvariable=self.name_columns).grid(row=0, column=1)

        tk.Label(columns_frame, text="Business Location Columns", width=20, anchor='w').grid(row=1, column=0)
        tk.Entry(columns_frame, width=30, textvariable=self.location_columns).grid(row=1, column=1)

        return columns_frame

    def create_options_frame(self):
        """
        Creates a frame that contains the widgets necessary for choosing which services are used and specifying api
        keys.

        :return options_frame: the frame used for choosing which services are used and specifying api keys
        """

        # creates the options frame
        options_frame = tk.Frame(master=self)

        # adds Facebook access token label and entry box to the options frame
        tk.Label(options_frame, text="Facebook Access Token", anchor='w').grid(row=0, column=0)
        tk.Entry(options_frame, width=32, textvariable=self.facebook_access_token).grid(row=0, column=1)
        tk.Button(options_frame, command=lambda: self.get_key("facebook"), text="?").grid(row=0, column=2)

        # adds GeoNames username label and entry box to the options frame
        tk.Label(options_frame, text="GeoNames Username", anchor='w').grid(row=1, column=0)
        tk.Entry(options_frame, width=32, textvariable=self.geonames_username).grid(row=1, column=1)
        tk.Button(options_frame, command=lambda: self.get_key("geonames"), text="?").grid(row=1, column=2)

        # adds Yelp api key label and entry box to the options frame
        tk.Label(options_frame, text="Yelp API Key", anchor='w').grid(row=2, column=0)
        tk.Entry(options_frame, width=32, textvariable=self.yelp_api_key).grid(row=2, column=1)
        tk.Button(options_frame, command=lambda: self.get_key("yelp"), text="?").grid(row=2, column=2)

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

        # opens the location file
        location_file = open('data/locations.txt', 'w')

        # writes the locations to the locations file
        location_file.write(self.data_location_variable.get() + '\n')
        location_file.write(self.results_location_variable.get() + '\n')

        # opens the columns file
        columns_file = open('data/columns.txt', 'w')

        # write the column data to the columns file
        columns_file.write(self.name_columns.get() + '\n')
        columns_file.write(self.location_columns.get() + '\n')

    def run(self):
        """
        Runs the Business classification algorithm based on the user settings.
        """

        # load the facebook web scraper
        self.facebook = facebook.Facebook(self.facebook_access_token.get(), self.geonames_username.get())

        # if facebook is not working
        if not self.facebook.test():

            # alert the user that their API keys are incorrect
            messagebox.showinfo("Incorrect API Keys",
                                "The entered Facebook access token or GeoNames username is incorrect.")

        # load the yelp web scraper
        self.yelp = yelp.Yelp(self.yelp_api_key.get())

        # if yelp is not working
        if not self.yelp.test():
            # alert the user that their API keys are incorrect
            messagebox.showinfo("Incorrect API Keys", "The entered Yelp API key is incorrect.")

        # load the google web scraper
        self.google = google.Google()

        # load the file reader and writer
        r = reader.FileReader(self.data_location_variable.get())
        w = writer.FileWriter(self.results_location_variable.get())

        # gets the name variable and splits up the columns
        name_ = self.name_columns.get().split(',')

        # initializes the names array to store indices
        names = []

        # iterates over the name_ array
        for n in name_:

            # appends the int loaded from storage to names
            names.append(int(n))

        # gets the locations variable and splits up the columns
        location_ = self.location_columns.get().split(',')

        # initializes the locations array to store indices
        locations = []

        # iterates over the location_ array
        for l in location_:

            # appends the index of the location to locations
            locations.append(int(l))

        # iterate over the read data
        for i in r:

            # initializes search variables
            name = ""
            location = ""

            # iterate over names
            for n in names:

                # add the next column to the name variable
                name += i[n] + " "

            for l in locations:

                # add the next column to the location variable
                location += i[l] + " "

            # write the data to the results file
            w.write([i[0], i[1]] +
                    self.facebook.get_category(name, location) +
                    self.google.get_category(name, location) +
                    self.yelp.get_category(name, location))

    def get_key(self, site):
        """
        Opens the help site for Facebook, Geonames, or Yelp for getting an API key.

        :param site: a string for which site the user wants to get an API key for
        """

        # if the site is facebook
        if site == 'facebook':

            # open the instructions to get a facebook API key
            webbrowser.open("https://developers.facebook.com/tools/accesstoken/")

        # if the site is yelp
        elif site == 'yelp':

            # open the instructions to get a yelp API key
            webbrowser.open("https://www.yelp.com/developers/documentation/v3/authentication")

        # if the site is geonames
        elif site == 'geonames':

            # open the instructions to sign up for a geonames account
            webbrowser.open("http://www.geonames.org/login")



# creates the tkinter root
root = tk.Tk()

# changes the title of the window to business classifier
root.title('Business Classifier')

# change the size of the main window
root.geometry('500x280')

# disallow the main window from being resized
root.resizable(False, False)

# creates the the application and starts the loop
app = Application(master=root)
app.mainloop()
