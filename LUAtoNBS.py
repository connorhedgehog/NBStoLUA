import pynbs
cnote = 0
nbsname = input("File to convert? Must be in the same folder as this script\n")
song = pynbs.read(nbsname)
tps = song.header.tempo
spt = 1 / tps
script = open("noteblock.lua", "w")
script.writelines('local speaker = peripheral.find(\"speaker\")\n')
script.close()
script = open("noteblock.lua", "a")
for x in song.notes:
  instrument = song.notes[cnote].instrument
  # there's a better way to do this!
  if instrument == 0:
    instrument = "harp"
  elif instrument == 1:
    instrument = "bass"
  elif instrument == 2:
    instrument == "basedrum"
  elif instrument == 3:
    instrument == "snare"
  elif instrument == 4:
    instrument == "hat"
  elif instrument == 5:
    instrument == "guitar"
  elif instrument == 6:
    instrument == "flute"
  elif instrument == 7:
    instrument == "bell"
  elif instrument == 8:
    instrument == "chime"
  elif instrument == 9:
    instrument == "xylophone"
  elif instrument == 10:
    instrument == "iron_xylophone"
  elif instrument == 11:
    instrument == "cow_bell"
  elif instrument == 12:
    instrument == "didgeridoo"
  elif instrument == 13:
    instrument == "bit"
  elif instrument == 14:
    instrument == "banjo"
  elif instrument == 15:
    instrument == "pling"
  script.write("speaker.playNote(\"{}\", 1, {})\n".format(instrument, song.notes[cnote].key - 33))
  if cnote == len(song.notes) - 1: 
    print("Should be done?")
  elif song.notes[cnote].tick != song.notes[cnote+1].tick:
    mmath = song.notes[cnote+1].tick - song.notes[cnote].tick
    mmmath = mmath * spt 
    script.write("sleep({})\n".format(mmmath))
  cnote += 1
input("Done!")
