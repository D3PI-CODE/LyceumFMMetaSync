# 🎙️ LyceumFMMetaSync

<div align="center">

[![Lyceum FM Logo](https://img.shields.io/badge/🎵-Lyceum%20FM-ff6b6b?style=for-the-badge)](https://www.mixcloud.com/Lyceum_FM/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/D3PI-CODE/LyceumFMMetaSync.git)
[![Python](https://img.shields.io/badge/Python-3.x-3776ab?style=for-the-badge&logo=python)](https://python.org)

**A sophisticated CLI application that synchronizes metadata from Lyceum FM's RadioDJ playlist to OBS via text files.**

*Bridging the gap between Google Sheets and OBS streaming software for dynamic broadcast information display.*

</div>

---

## 🎵 About Lyceum FM

**Lyceum FM** is the premier radio station of **Lyceum International School Nugegoda**, one of Sri Lanka's leading educational institutions. Our radio station serves as a dynamic platform for students to explore broadcasting, journalism, and media production while entertaining our community with quality programming.

### 🌟 What Makes Lyceum FM Special

- **Student-Driven Content**: Entirely managed and operated by talented students
- **Educational Excellence**: Part of Lyceum International School's commitment to holistic education
- **Community Impact**: Broadcasting quality content that resonates with our school community and beyond
- **Professional Training**: Providing real-world broadcasting experience to aspiring media professionals

### 🎧 Listen to Our Shows

<div align="center">

[![Listen on Mixcloud](https://img.shields.io/badge/🎵-Listen%20on%20Mixcloud-52c6ea?style=for-the-badge&logo=mixcloud)](https://www.mixcloud.com/Lyceum_FM/)

*Tune in to our latest broadcasts, mixes, and exclusive content*

</div>

## 🚀 Features

<div align="center">

| Feature | Description |
|---------|-------------|
| 🔄 **Real-time Sync** | Live metadata synchronization from Google Sheets |
| 🎵 **Smart Parsing** | Automatic song and artist information separation |
| 📺 **OBS Integration** | Direct compatibility with OBS streaming software |
| ⚙️ **Configurable** | Customizable refresh rates and settings |
| 🛡️ **Error Handling** | Robust error management and status logging |
| 🌍 **UTF-8 Support** | Full support for international characters |

</div>

## 📋 Prerequisites

- Python 3.x
- Google Sheets API access
- Public Google Spreadsheet with RadioDJ metadata
- The following Python packages:
  ```
  requests
  ```

## ⚙️ Configuration

1. Set up your Google Sheet:
   - Make the sheet public (Anyone with link can view)
   - Note down the Spreadsheet ID
   - Ensure metadata is in format: "Song Name - Artist Name"

2. Configure the script:
   ```python
   SPREADSHEET_ID = 'your-spreadsheet-id'
   SHEET_NAME = 'Sheet1'
   ROW_NUMBER = 1
   INTERVAL_MS = 1000
   API_KEY = 'your-api-key'
   ```

## 📦 Installation

### 🔗 Clone the Repository

```bash
git clone https://github.com/D3PI-CODE/LyceumFMMetaSync.git
cd LyceumFMMetaSync
```

### 📋 Install Dependencies

```bash
pip install requests
```

### ⚙️ Configure Your Settings

Update the configuration variables in the script with your API key and spreadsheet ID.

## 🔧 Usage

Run the script:
```bash
python LyceumFMMetaSync.py
```

The script will:
1. Monitor the specified Google Sheet row
2. Split song and artist information
3. Write to:
   - `current_song.txt`
   - `current_artist.txt`

## 🎬 OBS Setup

1. Add Text (GDI+) or (Freetype 2) sources to your scene
2. Check "Read from file"
3. Select the respective output files:
   - For song name: `current_song.txt`
   - For artist name: `current_artist.txt`

## 🤝 Contributing

We welcome contributions from the community! Feel free to:

- 🐛 **Report bugs** - Help us improve by reporting issues
- 💡 **Suggest features** - Share your ideas for new functionality  
- 🔧 **Submit pull requests** - Contribute code improvements
- 📖 **Improve documentation** - Help make our docs better

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

## 👨‍💻 Author

**Created by Aken Dep** for **Lyceum FM**

<div align="center">

[![GitHub Profile](https://img.shields.io/badge/GitHub-D3PI--CODE-181717?style=for-the-badge&logo=github)](https://github.com/D3PI-CODE)

*Crafted with ❤️ for the Lyceum FM broadcasting team*

</div>

---

<div align="center">

**🎙️ Lyceum FM - Revolutionizing the Soundwaves 🎙️**

*Part of Lyceum International School Nugegoda*

</div>
---
