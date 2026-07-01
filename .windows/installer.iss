#define Publisher "DeepThoughtt"
#define AppName "Esolang Interpreters"

[Setup]
AppName={#AppName}
AppVersion=0.1.0
AppVerName={#AppName}
AppPublisher={#Publisher}
DefaultDirName={pf}\{#AppName}
DefaultGroupName={#AppName}
ChangesEnvironment=yes
SetupIconFile=..\assets\icons\esolangs.ico

OutputDir=output
OutputBaseFilename=EsolangInterpreters-Windows-Installer
SetupIconFile=..\assets\icons\esolangs.ico
UninstallDisplayIcon={app}\esolangs.ico
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
LanguageDetectionMethod=locale

[Types]
Name: "full"; Description: "Install everything"
Name: "custom"; Description: "Choose which interpreters to install"; Flags: iscustom

[Components]
Name: "forreal"; Description: "4RL Interpreter"; Types: full custom; Flags: checkablealone
Name: "abcd"; Description: "ABCD Interpreter"; Types: full custom; Flags: checkablealone
Name: "boolfuck"; Description: "Boolfuck Interpreter"; Types: full custom; Flags: checkablealone
Name: "brainfuck"; Description: "Brainfuck Interpreter"; Types: full custom; Flags: checkablealone
Name: "infinitick"; Description: "Infinitick Interpreter"; Types: full custom; Flags: checkablealone
Name: "minibitmove"; Description: "MiniBitMove Interpreter"; Types: full custom; Flags: checkablealone
Name: "ministringfuck"; Description: "MiniStringFuck Interpreter"; Types: full custom; Flags: checkablealone
Name: "paintfuck"; Description: "Paintfuck Interpreter"; Types: full custom; Flags: checkablealone
Name: "smallfuck"; Description: "Smallfuck Interpreter"; Types: full custom; Flags: checkablealone
Name: "tick"; Description: "Tick Interpreter"; Types: full custom; Flags: checkablealone
Name: "ticker"; Description: "Ticker Interpreter"; Types: full custom; Flags: checkablealone

[Files]
Source: "..\dist\fr.exe"; DestDir: "{app}"; Components: forreal
Source: "..\dist\abcd.exe"; DestDir: "{app}"; Components: abcd
Source: "..\dist\boolfk.exe"; DestDir: "{app}"; Components: boolfuck
Source: "..\dist\bf.exe"; DestDir: "{app}"; Components: brainfuck
Source: "..\dist\itick.exe"; DestDir: "{app}"; Components: infinitick
Source: "..\dist\mbm.exe"; DestDir: "{app}"; Components: minibitmove
Source: "..\dist\msf.exe"; DestDir: "{app}"; Components: ministringfuck
Source: "..\dist\pf.exe"; DestDir: "{app}"; Components: paintfuck
Source: "..\dist\sf.exe"; DestDir: "{app}"; Components: smallfuck
Source: "..\dist\tick.exe"; DestDir: "{app}"; Components: tick
Source: "..\dist\ticker.exe"; DestDir: "{app}"; Components: ticker
Source: "..\assets\icons\esolangs.ico"; DestDir: "{app}"

[Icons]
Name: "{group}\Esolang Interpreters"; Filename: "{app}\fr.exe"; Components: forreal
Name: "{group}\Esolang Interpreters"; Filename: "{app}\abcd.exe"; Components: abcd
Name: "{group}\Esolang Interpreters"; Filename: "{app}\boolfk.exe"; Components: boolfuck
Name: "{group}\Esolang Interpreters"; Filename: "{app}\bf.exe"; Components: brainfuck
Name: "{group}\Esolang Interpreters"; Filename: "{app}\itick.exe"; Components: infinitick
Name: "{group}\Esolang Interpreters"; Filename: "{app}\mbm.exe"; Components: minibitmove
Name: "{group}\Esolang Interpreters"; Filename: "{app}\msf.exe"; Components: ministringfuck
Name: "{group}\Esolang Interpreters"; Filename: "{app}\pf.exe"; Components: paintfuck
Name: "{group}\Esolang Interpreters"; Filename: "{app}\sf.exe"; Components: smallfuck
Name: "{group}\Esolang Interpreters"; Filename: "{app}\tick.exe"; Components: tick
Name: "{group}\Esolang Interpreters"; Filename: "{app}\ticker.exe"; Components: ticker

[Environment]
Name: "PATH"; Value: "{app}"; Action: "prepend"; Flags: uninsdeletevalue
