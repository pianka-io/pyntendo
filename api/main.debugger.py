from dbg.debugger import Debugger
from emu.emulator import Emulator


emu = Emulator("pytendo", "bin/pals/2C02G.pal", "bin/tests/1.Branch_Basics.nes")
dbg = Debugger(emu)
dbg.run()
