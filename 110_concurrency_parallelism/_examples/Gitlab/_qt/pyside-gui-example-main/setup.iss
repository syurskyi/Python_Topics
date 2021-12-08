#define ApplicationVersion GetEnv('THISAPPLICATION_INSTALLER_VERSION')

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{45131461-F27C-48DC-AE29-4BDA32CBB3AC}
AppName=ThisApplication
AppVersion={#ApplicationVersion}
DefaultDirName={%USERPROFILE}\ThisApplication
DisableProgramGroupPage=yes
OutputDir={#SourcePath}\dist
OutputBaseFilename=Install_ThisApplication_v{#ApplicationVersion}
Compression=lzma
SolidCompression=yes
SetupIconFile={#SourcePath}\res\install_icon.ico
ChangesEnvironment=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "{#SourcePath}\dist\ThisApplication\ThisApplication.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SourcePath}\dist\ThisApplication\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\ThisApplication"; Filename: "{app}\ThisApplication.exe"
Name: "{commondesktop}\ThisApplication"; Filename: "{app}\ThisApplication.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\ThisApplication.exe"; Description: "{cm:LaunchProgram,ThisApplication}"; Flags: nowait postinstall

[Code]
var
  EnvironmentPage: TInputQueryWizardPage;

procedure AddEnvironmentPage();
begin
  EnvironmentPage := CreateInputQueryPage(
    wpSelectDir,
    'Configure Environment',
    'Evironment variables can be changed in Windows (via Advanced System Settings) at any time.', '');
  EnvironmentPage.Add('THISAPPLICATION_TESTVAR', False);
  EnvironmentPage.Values[0] := GetEnv('THISAPPLICATION_TESTVAR');
  if EnvironmentPage.Values[0] = '' then EnvironmentPage.Values[0] := 'something';
end;

procedure InitializeWizard();
begin
  AddEnvironmentPage();
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    RegWriteStringValue(HKEY_CURRENT_USER, 'Environment', 'THISAPPLICATION_TESTVAR', EnvironmentPage.Values[0]);
  end;
end;
