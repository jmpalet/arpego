<template>
  <div>
    <ul class="set">
      <li class="white c" @click="handler('C', 'C')"></li>
      <li class="black ds" @click="handler('C#', 'Db')"></li>
      <li class="white d" @click="handler('D', 'D')"></li>
      <li class="black es" @click="handler('D#', 'Eb')"></li>
      <li class="white e" @click="handler('E', 'E')"></li>
      <li class="white f" @click="handler('F', 'F')"></li>
      <li class="black gs" @click="handler('F#', 'Gb')"></li>
      <li class="white g" @click="handler('G', 'G')"></li>
      <li class="black as" @click="handler('G#', 'Ab')"></li>
      <li class="white a" @click="handler('A', 'A')"></li>
      <li class="black bs" @click="handler('A#', 'Bb')"></li>
      <li class="white b" @click="handler('B', 'B')"></li>
    </ul>

    <div class="choice-list">
      <button class="choice" v-on:click="changeInstrument('guitar')">Guitar</button>
      <button class="choice" v-on:click="changeInstrument('ukulele')">Ukulele</button>
    </div>

    <div class="diagram-wrap" v-show="instrument=='guitar'">
        <div class="diagram">
          <div class="strings">
            <div class="row first">
              <div class="cell fret"><div class="note" v-show="showNote(1,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,1)"></div></div>
            </div>
            <div class="row">
              <div class="cell fret"><div class="note" v-show="showNote(1,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,2)"></div></div>
            </div>
            <div class="row">
              <div class="cell fret"><div class="note" v-show="showNote(1,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,3)"></div></div>
            </div>
            <div class="row">
              <div class="cell fret"><div class="note" v-show="showNote(1,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,4)"></div></div>
            </div>
            <div class="row">
              <div class="cell fret"><div class="note" v-show="showNote(1,5)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,5)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,5)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,5)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,5)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,5)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,5)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,5)"></div></div>
            </div>
            <div class="row last">
              <div class="cell fret"><div class="note" v-show="showNote(1,6)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,6)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,6)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,6)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,6)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,6)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,6)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,6)"></div></div>
            </div>
          </div>
          <h3 class="chordname">{{ chordName }}</h3>                          
        </div>
    </div>

    <div class="diagram-wrap" v-show="instrument=='ukulele'">
        <div class="diagram">
          <div class="strings">
            <div class="row first">
              <div class="cell fret"><div class="note" v-show="showNote(1,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,1)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,1)"></div></div>
            </div>
            <div class="row">
              <div class="cell fret"><div class="note" v-show="showNote(1,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,2)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,2)"></div></div>
            </div>
            <div class="row">
              <div class="cell fret"><div class="note" v-show="showNote(1,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,3)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,3)"></div></div>
            </div>
            <div class="row last">
              <div class="cell fret"><div class="note" v-show="showNote(1,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(2,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(3,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(4,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(5,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(6,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(7,4)"></div></div>
              <div class="cell fret"><div class="note" v-show="showNote(8,4)"></div></div>
            </div>
          </div>
          <h3 class="chordname">{{ chordName }}</h3>                          
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Tone from 'tone'
export default {
  data () {
    return {
      instrument: 'guitar',
      note: null,
      chord: [],
      chordName: null,
      keyCode: '',
    }
  },
  methods: {
    handler (name, note, scale = 4) {
      this.playTone(note, scale)
      this.getChord(note)
      this.note = note
      this.chordName = name
    },
    changeInstrument (instrument) {
      this.instrument = instrument
      this.getChord(this.note)
    },
    playTone (note, scale) {
      var synth = new Tone.Synth({
        "oscillator" : {
          "type" : "amtriangle",
          "harmonicity" : 0.5,
          "modulationType" : "sine"
        },
        "envelope" : {
          "attackCurve" : 'exponential',
          "attack" : 0.05,
          "decay" : 0.4,
          "sustain" : 0.2,
          "release" : 1.5,
        },
        "portamento" : 0.05
      }).toMaster();
      synth.triggerAttackRelease(note + scale, "8n");
    },
    getChord (note) {
      if (note === null) {
        return false
      }
      const path = 'https://arpego-api.herokuapp.com/api/chord/' + this.instrument + '/'
      axios.get(path + note.replace("#", "s").toLowerCase())
      .then(response => {
        this.chord = response.data
      })
      .catch(error => {
        console.log(error)
      })
    },
    showNote (fret, string) {
      for (var i = 0; i < this.chord.length; i++) { 
        if (this.chord[i]['fret'] == fret && this.chord[i]['string'] == string) {
          return true;
        }
      }
    },
    onkey (event) {
      switch(event.key) {
        case "z":
        case "y":
          this.handler('C', 'C');
          break;
        case "s":
          this.handler('C#', 'Db');
          break;
        case "x":
          this.handler('D', 'D');
          break;
        case "d":
          this.handler('D#', 'Eb');
          break;
        case "c":
          this.handler('E', 'E');
          break;
        case "v":
          this.handler('F', 'F');
          break;
        case "g":
          this.handler('F#', 'Gb');
          break;
        case "b":
          this.handler('G', 'G');
          break;
        case "h":
          this.handler('G#', 'Ab');
          break;
        case "n":
          this.handler('A', 'A');
          break;
        case "j":
          this.handler('A#', 'Bb');
          break;
        case "m":
          this.handler('B', 'B');
          break;                                          
        default:
          break;
        }
    }
  },
  created: function () {
    window.addEventListener('keydown', this.onkey)
  },
  beforeDestroy: function () {
    window.removeEventListener('keydown', this.onkey)
  },
}
</script>