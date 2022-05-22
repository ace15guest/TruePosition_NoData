from tkinter import *
from tkinter import ttk, messagebox
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Generation.GraphGenerator import ScatterPlot
import tkinter.filedialog as fd
from InputFile.Parse import DataCollectFROMCSV
from Analysis.UpAnalyasis import AllowableUps
from PIL import ImageTk, Image
from Analysis.DataError import Radial_Error


# noinspection PyAttributeOutsideInit
# noinspection PyAttributeOutsideInit,DuplicatedCode
class GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x750")
        self.root.resizable(0, 0)
        ########################
        # Initialize Variables #
        ########################
        self.filePaths = []
        self.up_values = [1]

        ####################
        # Build The Window #
        ####################
        self.BrowsePlace()
        self.ParamPlace()
        self.AdditionalParamPlace()
        self.CalculationsPlace()
        self.InitPlotsPlace()
        self.ScrollBarPlace()
        self.NxtPrvGenPlace()

        ###################
        # Show the Window #
        ###################
        self.root.mainloop()

    #######################
    # Placement Functions #
    #######################
    def BrowsePlace(self):
        """
        Place Browse, Clear, and entry on the Screen
        :return:
        """
        # FILE LIST VARIABLE
        self.file_list_var = StringVar()
        self.file_list_var.set("Select One Or Multiple Files")
        # FILE ENTRY/ BROWSE BTN / CLEAR BTN
        self.file_entry = Entry(self.root, textvariable=self.file_list_var, width=int(1400 / 20))
        browse_btn = Button(self.root, text="Browse...", command=self.Browse)
        clear_btn = Button(self.root, text="Reset", command=self.Reset)
        # PLACE BUTTONS AND ENTRY
        self.file_entry.place(x=10, y=20)
        browse_btn.place(x=440, y=17)
        clear_btn.place(x=500, y=17)

    def ParamPlace(self):
        """
        Place Point Style, Point Size, Scale Factor
        :return: None
        """
        marks = ['x', 'X', '.', ',', 'o', 'v', 'v', '<', '>', 's',
                 'p', 'P', '*', 'h', 'H', '+', '1', '2', '3', '5', '8']
        point_sizes = list(np.arange(10, 151, 1))
        # MARKER Type
        self.mark_i_val = StringVar()
        self.mark_m_val = StringVar()
        # Marker Initialize
        self.mark_i_val.set(marks[0])
        self.mark_m_val.set(marks[4])
        # POINT SIZE/ SCALE FACTOR/ MARK
        self.meas_marker_var = StringVar()
        self.ideal_marker_var = StringVar()
        self.meas_pt_size_var = StringVar()
        self.ideal_pt_size__var = StringVar()
        self.scale_factor_var = StringVar()
        # Initialize Marker Size
        self.meas_pt_size_var.set('50')
        self.ideal_pt_size__var.set('50')
        # Labels
        scale_factor_label = Label(self.root, text="Scale Factor")
        meas_label = Label(self.root, text="Measured")
        ideal_label = Label(self.root, text="Ideal")
        point_style_label = Label(self.root, text="Point Style")
        point_size_label = Label(self.root, text="Point Size")
        # Place Labels
        scale_factor_label.place(x=350, y=50)
        meas_label.place(x=5, y=80)
        ideal_label.place(x=10, y=110)
        point_style_label.place(x=80, y=50)
        point_size_label.place(x=210, y=50)
        # Option/Spin Boxes
        self.meas_mark_opt = OptionMenu(self.root, self.meas_marker_var, *marks)
        self.ideal_mark_opt = OptionMenu(self.root, self.ideal_marker_var, *marks)
        self.scale_factor_spin = Spinbox(self.root, from_=1, to=500, increment=1, textvariable=self.scale_factor_var)
        self.meas_size_combo = ttk.Combobox(self.root, values=point_sizes, textvariable=self.meas_pt_size_var)
        self.ideal_size_combo = ttk.Combobox(self.root, values=point_sizes, textvariable=self.ideal_pt_size__var)
        # Place Option Boxes Spin
        self.meas_mark_opt.place(x=80, y=70, width=70)
        self.ideal_mark_opt.place(x=80, y=100, width=70)
        self.scale_factor_spin.place(x=350, y=85)
        self.meas_size_combo.place(x=170, y=75)
        self.ideal_size_combo.place(x=170, y=105)
        return None

    def AdditionalParamPlace(self):
        """

        :return:
        """
        # Maximum/Least material Condition Variables
        self.max_mat_chk_var = IntVar()
        self.least_mat_chk_var = IntVar()
        self.up_chk_var = IntVar()
        # MMC LMC Create
        self.max_mat_chk_btn = Checkbutton(self.root, text="MMC", variable=self.max_mat_chk_var, onvalue=1,
                                           offvalue=0, command=self.MMCButton)
        self.least_mat_chk_btn = Checkbutton(self.root, text="LMC", variable=self.least_mat_chk_var, onvalue=1,
                                             offvalue=0, command=self.LMCButton)
        self.up_chk_btn = Checkbutton(self.root, text="Up-Analysis", variable=self.up_chk_var, onvalue=1,
                                      offvalue=0, command=self.UpsButton)
        # MMC LMC Place
        self.max_mat_chk_btn.place(x=230, y=160)
        self.least_mat_chk_btn.place(x=40, y=160)
        self.up_chk_btn.place(x=410, y=160)

    def CalculationsPlace(self):
        """
        Places Calculated Data on the screen
        :return:
        """
        # Label Frames
        holistic_label_frame = LabelFrame(self.root, text="Holistic \u00B0", height=100, width=600)
        current_up_label_frame = LabelFrame(self.root, text="Current Up", height=100, width=600)
        # Place Label Frames
        holistic_label_frame.place(x=20, y=250)
        current_up_label_frame.place(x=20, y=350)
        # HOLISTIC LABELS
        radial_error_hlstc_label = Label(self.root, text="Radial Error")
        radial_error_ave_hlstc_label = Label(self.root, text="Ave:")
        radial_error_max_hlstc_label = Label(self.root, text="Max:")
        radial_error_3sig_hlstc_label = Label(self.root, text="3-\u03c3 Limit")
        percent_over_hlstc_label = Label(self.root, text="Percent Oversize")
        percent_over_ave_hlstc_label = Label(self.root, text="Ave:")
        percent_over_x_hlstc_label = Label(self.root, text="X:")
        percent_over_y_hlstc_label = Label(self.root, text="Y:")
        diameter_hlstc_label = Label(self.root, text="Diameter")
        diameter_ave_hlstc_label = Label(self.root, text="Ave:")
        diameter_max_hlstc_label = Label(self.root, text="Max:")
        diameter_min_hlstc_label = Label(self.root, text="Min:")
        # UP LABELS
        radial_error_up_label = Label(self.root, text="Radial Error")
        radial_error_ave_up_label = Label(self.root, text="Ave:")
        radial_error_max_up_label = Label(self.root, text="Max:")
        radial_error_min_up_label = Label(self.root, text="3-\u03c3 Limit")
        percent_over_up_label = Label(self.root, text="Percent Oversize")
        percent_over_ave_up_label = Label(self.root, text="Ave:")
        percent_over_x_up_label = Label(self.root, text="X:")
        percent_over_y_up_label = Label(self.root, text="Y:")
        diameter_up_label = Label(self.root, text="Diameter")
        diameter_ave_up_label = Label(self.root, text="Ave:")
        diameter_max_up_label = Label(self.root, text="Max:")
        diameter_min_up_label = Label(self.root, text="Min:")
        # PLACE HOLISTIC LABELS
        radial_error_hlstc_label.place(x=30, y=265)
        radial_error_ave_hlstc_label.place(x=30, y=285)
        radial_error_max_hlstc_label.place(x=30, y=300)
        radial_error_3sig_hlstc_label.place(x=30, y=315)
        percent_over_hlstc_label.place(x=280, y=265)
        percent_over_ave_hlstc_label.place(x=280, y=285)
        percent_over_x_hlstc_label.place(x=280, y=300)
        percent_over_y_hlstc_label.place(x=280, y=315)
        diameter_hlstc_label.place(x=520, y=265)
        diameter_ave_hlstc_label.place(x=520, y=285)
        diameter_max_hlstc_label.place(x=520, y=300)
        diameter_min_hlstc_label.place(x=520, y=315)
        # PLACE UP LABELS
        radial_error_up_label.place(x=30, y=365)
        radial_error_ave_up_label.place(x=30, y=385)
        radial_error_max_up_label.place(x=30, y=400)
        radial_error_min_up_label.place(x=30, y=415)
        percent_over_up_label.place(x=280, y=365)
        percent_over_ave_up_label.place(x=280, y=385)
        percent_over_x_up_label.place(x=280, y=400)
        percent_over_y_up_label.place(x=280, y=415)
        diameter_up_label.place(x=520, y=365)
        diameter_ave_up_label.place(x=520, y=385)
        diameter_max_up_label.place(x=520, y=400)
        diameter_min_up_label.place(x=520, y=415)

    def InitPlotsPlace(self):
        """

        :return:
        """
        # Place Large Empty Plot On Right Hand of Screen
        self.canvas = FigureCanvasTkAgg(ScatterPlot(), self.root)
        self.canvas.get_tk_widget().place(x=800, y=-25, height=650, width=650)
        self.canvas.draw()
        toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        toolbar.place(x=1015, y=555)
        # Place Histograms on Screen
        # img = ImageTk.PhotoImage(Image.open("Assets/init_hist"))
        #
        # # Create a Label Widget to display the text or Image
        # label = Label(self.root, image=img)
        # label.image = img
        # label.place(x=20,y=40)
        img = Image.open('Assets/init_hist')
        img = img.resize((300, 300))
        #
        # img1 = PIL_imagetk.PhotoImage(file="C:\\Two.jpg")
        # img1 = img1._PhotoImage__photo.zoom(2)
        # label = Label(self.root, image=img1)
        # label.pack()

        photo = ImageTk.PhotoImage(img)

        label = Label(image=photo)
        label2 = Label(image=photo)

        label.image = photo
        label2.image = photo

        label.place(x=20, y=450)
        label2.place(x=310, y=450)

    def ScrollBarPlace(self):
        self.scroll_label_frame = LabelFrame(self.root, text="Ups")
        self.scroll_label_frame.place(x=620, y=44, width=260, height=540)
        text = Text(self.scroll_label_frame, wrap="none")
        scroll = Scrollbar(self.scroll_label_frame, orient="vertical", command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill="y")
        text.pack(fill=Y, expand=True)

    def NxtPrvGenPlace(self):
        """

        :return:
        """
        # Create NEXT/PREVIOUS/ASIS/TRBF/GENERATE Buttons
        next_button = Button(self.root, text="Next", width=10)
        prev_button = Button(self.root, text="Previous", width=10)
        asis_button = Button(self.root, text="As Is", width=10)
        trbf_button = Button(self.root, text="Trans-Rot BF", width=10)
        generate_button = Button(self.root, text="Generate", width=22, command=self.Generation)
        export_button = Button(self.root, text="Export", width=22)
        # Create TRBF Check Button
        self.export_trbf_var = IntVar()
        trbf_export_chkbtn = Checkbutton(self.root, text="Export TRBF", variable=self.export_trbf_var,
                                         onvalue=1, offvalue=1)
        # Place Buttons
        next_button.place(x=896 + 240, y=620)
        prev_button.place(x=814 + 240, y=620)
        asis_button.place(x=724 + 240, y=621)
        trbf_button.place(x=984 + 240, y=620)
        generate_button.place(x=813 + 240, y=660)
        export_button.place(x=813 + 240, y=690)
        # Place TRBF Check Button
        trbf_export_chkbtn.place(x=900, y=690)

    ####################
    # Temporary Checks #
    ####################
    def UpsButton(self):
        self.up_value_var = IntVar()

        if self.up_chk_var.get() == 1:
            self.ups_label = Label(self.root, text="Ups")
            self.ups_label.place(x=410, y=180)
            self.up_list_values = StringVar()
            self.up_list_values.set("")
            self.up_option = OptionMenu(self.root, self.up_list_values, *self.up_values)
            self.up_option.place(x=415, y=205)

        elif self.up_chk_var.get() == 0:
            self.ups_label.destroy()
            self.up_option.destroy()

    def MMCButton(self):
        if self.max_mat_chk_var.get() == 1:
            self.least_mat_chk_btn.config(state=DISABLED)

            self.maxspec_m = StringVar()
            self.minspec_m = StringVar()
            self.mmc_peg_val = IntVar()

            self.max_mmc = Entry(self.root, textvariable=self.maxspec_m, width=10)
            self.min_mmc = Entry(self.root, textvariable=self.minspec_m, width=10)
            self.mmcmin = Label(self.root, text="Min")
            self.mmcmax = Label(self.root, text="Max")
            self.mmc_peg = Radiobutton(self.root, text="Peg", variable=self.mmc_peg_val, value=0)
            self.mmc_hole = Radiobutton(self.root, text="Hole", variable=self.mmc_peg_val, value=1)

            self.min_mmc.place(x=235, y=205)
            self.mmcmin.place(x=230, y=180)
            self.max_mmc.place(x=320, y=205)
            self.mmcmax.place(x=320, y=180)
            self.mmc_peg.place(x=320, y=230)
            self.mmc_hole.place(x=230, y=230)
        else:

            self.least_mat_chk_btn.config(state=NORMAL)
            self.max_mmc.destroy()
            self.min_mmc.destroy()
            self.mmcmin.destroy()
            self.mmcmax.destroy()
            self.mmc_peg.destroy()
            self.mmc_hole.destroy()
        pass

    def LMCButton(self):
        if self.least_mat_chk_var.get() == 1:

            self.max_mat_chk_btn.config(state=DISABLED)
            self.maxspec_l = StringVar()
            self.minspec_l = StringVar()

            self.max_lmc = Entry(self.root, textvariable=self.maxspec_l, width=10)
            self.min_lmc = Entry(self.root, textvariable=self.minspec_l, width=10)
            self.lmcmin = Label(self.root, text="Min")
            self.lmcmax = Label(self.root, text="Max")

            self.lmcmin.place(x=40, y=180)
            self.lmcmax.place(x=130, y=180)
            self.max_lmc.place(x=45, y=205)
            self.min_lmc.place(x=130, y=205)

        else:

            self.max_mat_chk_btn.config(state=NORMAL)
            self.max_lmc.destroy()
            self.min_lmc.destroy()
            self.lmcmin.destroy()
            self.lmcmax.destroy()
        pass

    ####################
    # Button Functions #
    ####################
    def Browse(self):
        # Reset The up analysis if the previous state was disabled

        self.up_chk_btn.configure(state='normal')
        # Open the file dialog and only allow comma separated values
        files = fd.askopenfilenames(filetypes=[('comma separated values', '*.csv')])
        file_string = self.root.tk.splitlist(files)
        self.filePaths.clear()
        # Add files to list
        for file in file_string:
            self.filePaths.append(file)
        self.file_list_var.set(str(self.filePaths))
        # Pre Screen Up Checks
        if len(self.filePaths) > 1:
            for file in self.filePaths:
                try:
                    if temp == len(DataCollectFROMCSV(file)[0]):
                        pass
                    else:
                        unequal_pts_msg = messagebox.askquestion('Non-Equal Points', 'The documents selected have an '
                                                                                     'unequal amount of points. Up '
                                                                                     'Analysis is not available. '
                                                                                     '\nContinue?', icon='warning')
                        if unequal_pts_msg == 'no':
                            self.filePaths.clear()
                            self.file_list_var.set("Select One Or Multiple Files")
                        else:
                            self.up_chk_btn.configure(state='disabled')

                except NameError:
                    temp = len(DataCollectFROMCSV(file)[0])
            self.up_values = AllowableUps(temp)
        else:
            self.up_values = AllowableUps(len(DataCollectFROMCSV(self.filePaths[0])[0]))

    def Reset(self):
        self.file_list_var.set("Select One Or Multiple Files")
        self.canvas.get_tk_widget().destroy()
        self.InitPlotsPlace()
        self.ScrollBarPlace()

    def Generation(self):
        # Check If we must do Up-Analysis
        if self.up_chk_var.get() == 0:
            for file in self.filePaths:
                XI, XM, YI, YM, DM = DataCollectFROMCSV(file)


test = Tk()
GUI(test)
