"""
yt-dlp-ctk - GUI for yt-dlp

Copyright (C) 2023 Mikael Tranbom

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import customtkinter as ctk
# import yt_dlp


class MainTabs(ctk.CTkTabview):
    """Main Tabs"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Events
        def on_download_button_press():
            """On download button press"""

        def on_queue_button_press():
            """On add to queue button press"""

        # Create tabs
        self.add("Main")
        self.add("History")
        # self.add("Queue")
        # self.add("Sync")
        self.add("Settings")

        # Main tab
        self.label = ctk.CTkLabel(
            master=self.tab('Main'),
            text="Add links to download\n"
            "(separated by lines, spaces, comma or semicolon)"
        )
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.grid_rowconfigure(1, weight=1)
        self.links_textbox = ctk.CTkTextbox(master=self.tab('Main'), width=560)
        self.links_textbox.grid(row=1, column=0, padx=20, pady=10)

        self.download_settings_frame = ctk.CTkFrame(master=self.tab('Main'))
        self.download_settings_frame.grid(row=2, column=0, padx=10, pady=10)

        # self.audio_format_frame = ctk.CTkFrame(master=self.download_settings_frame)
        # self.audio_format_frame.grid(row=0, column=0, padx=10, pady=10)

        # self.audio_format_label = ctk.CTkLabel(
        #     master=self.audio_format_frame,
        #     text='Audio format'
        # )
        # self.audio_format_label.grid(row=0, column=0, padx=5, pady=5)

        self.audio_format_combobox = ctk.CTkComboBox(
            # self.audio_format_frame,
            self.download_settings_frame,
            values=['mp3', 'wav', 'ogg'],
            state='disabled'
        )
        self.audio_format_combobox.grid(row=0, column=0, padx=5, pady=5)

        self.audio_only = ctk.BooleanVar(value=False)
        self.checkbox_audio_only = ctk.CTkCheckBox(
            master=self.download_settings_frame,
            text='Audio only',
            variable=self.audio_only,
            onvalue=True,
            offvalue=False
        )
        self.checkbox_audio_only.grid(row=0, column=1, padx=5, pady=5)

        self.video_format_combobox = ctk.CTkComboBox(
            self.download_settings_frame,
            values=['mp4', 'mkv'],
            state='disabled'
        )
        self.video_format_combobox.grid(
            row=1, column=0, padx=5, pady=5
        )

        self.download_destination_dir_label = ctk.CTkLabel(
            master=self.download_settings_frame,
            text='Destination directory:'
        )
        self.download_destination_dir_label.grid(
            row=2, column=0, padx=5, pady=5
        )

        self.download_destination_dir_entry = ctk.CTkEntry(
            master=self.download_settings_frame,
            width=350
            # Add default destination dir + suffix
        )
        self.download_destination_dir_entry.grid(
            row=2, column=1, padx=5, pady=5
        )

        self.button_frame = ctk.CTkFrame(master=self.tab('Main'))
        self.button_frame.grid(row=4, column=0, padx=10, pady=10)
        self.download_now_button = ctk.CTkButton(
            self.button_frame, text='Download now', command=on_download_button_press
        )
        self.download_now_button.grid(row=0, column=0, padx=10, pady=10)

        self.add_to_queue_button = ctk.CTkButton(
            self.button_frame, text='Add to queue', command=on_queue_button_press
        )
        self.add_to_queue_button.grid(row=0, column=1, padx=10, pady=10)

        self.queue_label = ctk.CTkLabel(
            master=self.tab('Main'),
            text="Queued downloads"
        )
        self.queue_label.grid(row=0, column=1, padx=20, pady=10)

        self.queue_textbox = ctk.CTkTextbox(master=self.tab('Main'), width=560)
        self.queue_textbox.grid(row=1, column=1, padx=20, pady=20)

        # History tab
        self.history_textbox = ctk.CTkTextbox(
            master=self.tab('History'), height=400, width=1160
        )
        self.history_textbox.grid(row=1, column=0, padx=20, pady=20)

        # Settings tab
        self.destination_folder_label = ctk.CTkLabel(
            master=self.tab('Settings'),
            text="Default download destination"
        )
        self.destination_folder_label.grid(row=0, column=0, padx=20, pady=10)

        # Add icon showing if path is valid or invalid
        # Save button probably not needed, just update path on text entry
        # Disable field during active download
        self.destination_folder_textbox = ctk.CTkEntry(
            master=self.tab('Settings'), width=400
        )
        self.destination_folder_textbox.grid(row=1, column=0, padx=20, pady=10)

        # self.create_subfolder_channel
        # self.create_subfolder_playlist


class App(ctk.CTk):
    """App"""
    destination_dir: str

    def __init__(self):
        super().__init__()

        self.title("yt-dlp-gui")
        self.geometry('1260x690')

        self.tab_view = MainTabs(master=self, width=1220, height=650)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


def main():
    """Main function"""
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
