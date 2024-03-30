# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['PageMain.py'],
             pathex=['background_image.py', 'PageDrugManage.py', 'PageHome.py', 'PageLogin.py', 'PagePayFee.py', 'PagePrescriptionManage.py', 'PageQuery.py', 'PageRegister.py', 'PageSetting.py', 'ui_addDepart.py', 'ui_addDoctor.py', 'ui_addDrug.py', 'ui_addOperator.py', 'ui_addPrescription.py', 'ui_deleteDrug.py', 'ui_departNum.py', 'ui_departPresc.py', 'ui_doctorPrep.py', 'ui_drugMangage.py', 'ui_editPrescription.py', 'ui_home.py', 'ui_login.py', 'ui_pay.py', 'ui_prescriptionManage.py', 'ui_query.py', 'ui_register.py', 'ui_register_reg.py', 'ui_register_sec.py', 'ui_setDepart.py', 'ui_setDoctor.py', 'ui_setDrugPrice.py', 'ui_setDrugStock.py', 'ui_setOperator.py', 'ui_setPage.py'],
             binaries=[],
             datas=[],
             hiddenimports=['sys', 'Pyside6.QtWidgets', 'Pyside6.QtCore', 'Pyside6.QtGui'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='PageMain',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PageMain')
