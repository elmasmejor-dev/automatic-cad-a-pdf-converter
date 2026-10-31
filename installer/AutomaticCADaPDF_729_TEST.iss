#define AppVersion "7.2.9"
#define AppName "Automatic CAD a PDF Converter - Prueba 7.2.9"
[Setup]
AppId={{16B6B4CD-91A4-44F1-AC49-1E539A472729}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName}
AppPublisher=Manu
DefaultDirName={localappdata}\Programs\Automatic CAD a PDF Converter Test 729
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
OutputDir=..\out
OutputBaseFilename=Setup_Automatic_CAD_a_PDF_Converter_v7_2_9_PRUEBA
SetupIconFile=..\app-src\galleta.ico
UninstallDisplayIcon={app}\Automatic CAD a PDF Converter.exe
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
CloseApplications=yes
RestartApplications=no
UsePreviousAppDir=no
[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Accesos directos:"; Flags: checkedonce
[Files]
Source: "..\dist\Automatic CAD a PDF Converter\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
[Icons]
Name: "{autoprograms}\{#AppName}"; Filename: "{app}\Automatic CAD a PDF Converter.exe"; IconFilename: "{app}\galleta.ico"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\Automatic CAD a PDF Converter.exe"; IconFilename: "{app}\galleta.ico"; Tasks: desktopicon
[Run]
Filename: "{app}\Automatic CAD a PDF Converter.exe"; Description: "Abrir {#AppName}"; Flags: nowait postinstall skipifsilent
