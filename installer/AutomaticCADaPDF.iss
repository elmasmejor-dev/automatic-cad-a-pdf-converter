#define AppVersion "7.2.6"
#define AppName "Automatic CAD a PDF Converter"

[Setup]
AppId={{7EE6F382-156A-50F4-A1F1-01D7C20BE3F9}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher=Manu
DefaultDirName={localappdata}\Programs\Automatic CAD a PDF Converter
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
OutputDir=..\out
OutputBaseFilename=Setup_Automatic_CAD_a_PDF_Converter_v7_2_6
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
Name: "desktopicon"; Description: "Crear un acceso directo en el escritorio"; GroupDescription: "Accesos directos:"; Flags: checkedonce

[Files]
Source: "..\dist\Automatic CAD a PDF Converter\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\Automatic CAD a PDF Converter"; Filename: "{app}\Automatic CAD a PDF Converter.exe"; IconFilename: "{app}\galleta.ico"
Name: "{autodesktop}\Automatic CAD a PDF Converter"; Filename: "{app}\Automatic CAD a PDF Converter.exe"; IconFilename: "{app}\galleta.ico"; Tasks: desktopicon

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Uninstall\AutomaticCadPdfConverter"; Flags: deletekey

[Run]
Filename: "{app}\Automatic CAD a PDF Converter.exe"; Description: "Abrir Automatic CAD a PDF Converter"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}\runtime"
