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
      <button class="choice" v-bind:class="{ active: this.instrument === 'guitar' }" v-on:click="changeInstrument('guitar')">Guitar</button>
      <button class="choice" v-bind:class="{ active: this.instrument === 'ukulele' }" v-on:click="changeInstrument('ukulele')">Ukulele</button>
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
      map: {
        guitar: {
          1: {
            0: 'E3',
            1: 'F3',
            2: 'F#3',
            3: 'G3',
            4: 'G#3',
            5: 'A4',
            6: 'A#4',
            7: 'B4',
            8: 'C4',
          },
          2: {
            0: 'B3',
            1: 'C3',
            2: 'C#3',
            3: 'D3', 
            4: 'D#3',
            5: 'E3',
            6: 'F3',
            7: 'F#3',
            8: 'G3',
          },
          3: {
            0: 'G2',
            1: 'G#2',
            2: 'A3', 
            3: 'A#3',
            4: 'B3',
            5: 'C3',
            6: 'C#3',
            7: 'D3',
            8: 'D#3',
          },
          4: {
            0: 'D2',
            1: 'D#2',
            2: 'E2', 
            3: 'F2',
            4: 'F#2',
            5: 'G2',
            6: 'G#2',
            7: 'A3',
            8: 'A#3',
          },
          5: {
            0: 'A2',
            1: 'A#2',
            2: 'B#2', 
            3: 'C2',
            4: 'C#2',
            5: 'D2',
            6: 'D#2',
            7: 'E2',
            8: 'F2',
          },
          6: {
            0: 'E1',
            1: 'F1',
            2: 'F#1', 
            3: 'G1',
            4: 'G#1',
            5: 'A2',
            6: 'A#2',
            7: 'B2',
            8: 'C2',
          },
        },
        ukulele: {
          1: {
            0: 'A3',
            1: 'A#3',
            2: 'B3',
            3: 'C3',
            4: 'C#3',
            5: 'D3',
            6: 'D#3',
            7: 'E3',
            8: 'F3',
          },
          4: {
            0: 'G2',
            1: 'G#2',
            2: 'A3',
            3: 'A#3', 
            4: 'B3',
            5: 'C3',
            6: 'C#3',
            7: 'D3',
            8: 'D#3',
          },
          2: {
            0: 'E2',
            1: 'F2',
            2: 'F#2', 
            3: 'G2',
            4: 'G#2',
            5: 'A3',
            6: 'A#3',
            7: 'B3',
            8: 'C3',
          },
          3: {
            0: 'C2',
            1: 'C#2',
            2: 'D2', 
            3: 'D#2',
            4: 'E2',
            5: 'F2',
            6: 'F#2',
            7: 'G2',
            8: 'G#2',
          },
          4: {
            0: 'G2',
            1: 'G#2',
            2: 'A3',
            3: 'A#3', 
            4: 'B3',
            5: 'C3',
            6: 'C#3',
            7: 'D3',
            8: 'D#3',
          },
        }
      },
      samplers: {
        piano: {
          'A0': 'A0.[mp3|ogg]',
          'A1': 'A1.[mp3|ogg]',
          'A2': 'A2.[mp3|ogg]',
          'A3': 'A3.[mp3|ogg]',
          'A4': 'A4.[mp3|ogg]',
          'A5': 'A5.[mp3|ogg]',
          'A6': 'A6.[mp3|ogg]',
          'A#0': 'As0.[mp3|ogg]',
          'A#1': 'As1.[mp3|ogg]',
          'A#2': 'As2.[mp3|ogg]',
          'A#3': 'As3.[mp3|ogg]',
          'A#4': 'As4.[mp3|ogg]',
          'A#5': 'As5.[mp3|ogg]',
          'A#6': 'As6.[mp3|ogg]',
          'B0': 'B0.[mp3|ogg]',
          'B1': 'B1.[mp3|ogg]',
          'B2': 'B2.[mp3|ogg]',
          'B3': 'B3.[mp3|ogg]',
          'B4': 'B4.[mp3|ogg]',
          'B5': 'B5.[mp3|ogg]',
          'B6': 'B6.[mp3|ogg]',
          'C0': 'C0.[mp3|ogg]',
          'C1': 'C1.[mp3|ogg]',
          'C2': 'C2.[mp3|ogg]',
          'C3': 'C3.[mp3|ogg]',
          'C4': 'C4.[mp3|ogg]',
          'C5': 'C5.[mp3|ogg]',
          'C6': 'C6.[mp3|ogg]',
          'C7': 'C7.[mp3|ogg]',
          'C#0': 'Cs0.[mp3|ogg]',
          'C#1': 'Cs1.[mp3|ogg]',
          'C#2': 'Cs2.[mp3|ogg]',
          'C#3': 'Cs3.[mp3|ogg]',
          'C#4': 'Cs4.[mp3|ogg]',
          'C#5': 'Cs5.[mp3|ogg]',
          'C#6': 'Cs6.[mp3|ogg]',
          'D0': 'D0.[mp3|ogg]',
          'D1': 'D1.[mp3|ogg]',
          'D2': 'D2.[mp3|ogg]',
          'D3': 'D3.[mp3|ogg]',
          'D4': 'D4.[mp3|ogg]',
          'D5': 'D5.[mp3|ogg]',
          'D6': 'D6.[mp3|ogg]',
          'D#0': 'Ds0.[mp3|ogg]',
          'D#1': 'Ds1.[mp3|ogg]',
          'D#2': 'Ds2.[mp3|ogg]',
          'D#3': 'Ds3.[mp3|ogg]',
          'D#4': 'Ds4.[mp3|ogg]',
          'D#5': 'Ds5.[mp3|ogg]',
          'D#6': 'Ds6.[mp3|ogg]',
          'E0': 'E0.[mp3|ogg]',
          'E1': 'E1.[mp3|ogg]',
          'E2': 'E2.[mp3|ogg]',
          'E3': 'E3.[mp3|ogg]',
          'E4': 'E4.[mp3|ogg]',
          'E5': 'E5.[mp3|ogg]',
          'E6': 'E6.[mp3|ogg]',
          'F0': 'F0.[mp3|ogg]',
          'F1': 'F1.[mp3|ogg]',
          'F2': 'F2.[mp3|ogg]',
          'F3': 'F3.[mp3|ogg]',
          'F4': 'F4.[mp3|ogg]',
          'F5': 'F5.[mp3|ogg]',
          'F6': 'F6.[mp3|ogg]',
          'F#0': 'Fs0.[mp3|ogg]',
          'F#1': 'Fs1.[mp3|ogg]',
          'F#2': 'Fs2.[mp3|ogg]',
          'F#3': 'Fs3.[mp3|ogg]',
          'F#4': 'Fs4.[mp3|ogg]',
          'F#5': 'Fs5.[mp3|ogg]',
          'F#6': 'Fs6.[mp3|ogg]',
          'G0': 'G0.[mp3|ogg]',
          'G1': 'G1.[mp3|ogg]',
          'G2': 'G2.[mp3|ogg]',
          'G3': 'G3.[mp3|ogg]',
          'G4': 'G4.[mp3|ogg]',
          'G5': 'G5.[mp3|ogg]',
          'G6': 'G6.[mp3|ogg]',
          'G#0': 'Gs0.[mp3|ogg]',
          'G#1': 'Gs1.[mp3|ogg]',
          'G#2': 'Gs2.[mp3|ogg]',
          'G#3': 'Gs3.[mp3|ogg]',
          'G#4': 'Gs4.[mp3|ogg]',
          'G#5': 'Gs5.[mp3|ogg]',
          'G#6': 'Gs6.[mp3|ogg]'
        },
      },
      chords: {
        "guitar": {
            "ab": [
                {
                    "fret": 4,
                    "string": 1,
                },
                {
                    "fret": 4,
                    "string": 2,
                },
                {
                    "fret": 5,
                    "string": 3,
                },
                {
                    "fret": 6,
                    "string": 4,
                },
                {
                    "fret": 6,
                    "string": 5,
                },
                {
                    "fret": 4,
                    "string": 6,
                },
            ],
            "a": [
                {
                    "fret": 0,
                    "string": 1,
                },
                {
                    "fret": 2,
                    "string": 2,
                },
                {
                    "fret": 2,
                    "string": 3,
                },
                {
                    "fret": 2,
                    "string": 4,
                },
                {
                    "fret": 0,
                    "string": 5,
                },
                {
                    "fret": 0,
                    "string": 6,
                },
            ],
            "am": [
                {
                    "fret": 1,
                    "string": 2,
                },
                {
                    "fret": 2,
                    "string": 3,
                },
                {
                    "fret": 2,
                    "string": 4,
                },
            ],
            "bb": [
                {
                    "fret": 1,
                    "string": 1,
                },
                {
                    "fret": 3,
                    "string": 2,
                },
                {
                    "fret": 3,
                    "string": 3,
                },
                {
                    "fret": 3,
                    "string": 4,
                },
                {
                    "fret": 1,
                    "string": 5,
                },
            ],
            "b": [
                {
                    "fret": 0,
                    "string": 1,
                },
                {
                    "fret": 2,
                    "string": 1,
                },
                {
                    "fret": 4,
                    "string": 2,
                },
                {
                    "fret": 4,
                    "string": 3,
                },
                {
                    "fret": 4,
                    "string": 4,
                },
                {
                    "fret": 2,
                    "string": 5,
                },
                {
                    "fret": 0,
                    "string": 6,
                },
            ],
            "c": [
                {
                    "fret": 0,
                    "string": 1,
                },
                {
                    "fret": 1,
                    "string": 2,
                },
                {
                    "fret": 0,
                    "string": 3,
                },
                {
                    "fret": 2,
                    "string": 4,
                },
                {
                    "fret": 3,
                    "string": 5,
                },
                {
                    "fret": 0,
                    "string": 6,
                },
            ],
            "db": [
                {
                    "fret": 4,
                    "string": 1,
                },
                {
                    "fret": 6,
                    "string": 2,
                },
                {
                    "fret": 6,
                    "string": 3,
                },
                {
                    "fret": 6,
                    "string": 4,
                },
                {
                    "fret": 4,
                    "string": 5,
                },
                {
                    "fret": 4,
                    "string": 6,
                },
            ],
            "dm": [
                {
                    "fret": 1,
                    "string": 1,
                },
                {
                    "fret": 3,
                    "string": 2,
                },
                {
                    "fret": 2,
                    "string": 3,
                },
            ],
            "d": [
                {
                    "fret": 2,
                    "string": 1,
                },
                {
                    "fret": 3,
                    "string": 2,
                },
                {
                    "fret": 2,
                    "string": 3,
                },
                {
                    "fret": 0,
                    "string": 4,
                },
                {
                    "fret": 0,
                    "string": 5,
                },
                {
                    "fret": 0,
                    "string": 6,
                },
            ],
            "eb": [
                {
                    "fret": 6,
                    "string": 1,
                },
                {
                    "fret": 8,
                    "string": 2,
                },
                {
                    "fret": 8,
                    "string": 3,
                },
                {
                    "fret": 8,
                    "string": 4,
                },
                {
                    "fret": 6,
                    "string": 5,
                },
                {
                    "fret": 6,
                    "string": 6,
                },
            ],
            "em": [
                {
                    "fret": 0,
                    "string": 1,
                },
                {
                    "fret": 0,
                    "string": 2,
                },
                {
                    "fret": 0,
                    "string": 3,
                },
                {
                    "fret": 2,
                    "string": 4,
                },
                {
                    "fret": 2,
                    "string": 5,
                },
                {
                    "fret": 0,
                    "string": 6,
                },
            ],
            "e": [
                {
                    "fret": 0,
                    "string": 1,
                },
                {
                    "fret": 0,
                    "string": 2,
                },
                {
                    "fret": 1,
                    "string": 3,
                },
                {
                    "fret": 2,
                    "string": 4,
                },
                {
                    "fret": 2,
                    "string": 5,
                },
                {
                    "fret": 0,
                    "string": 6,
                },
            ],
            "fm": [
                {
                    "fret": 1,
                    "string": 1,
                },
                {
                    "fret": 1,
                    "string": 2,
                },
                {
                    "fret": 1,
                    "string": 3,
                },
                {
                    "fret": 3,
                    "string": 4,
                },
                {
                    "fret": 3,
                    "string": 5,
                },
                {
                    "fret": 1,
                    "string": 6,
                },
            ],
            "f": [
                {
                    "fret": 1,
                    "string": 1,
                },
                {
                    "fret": 1,
                    "string": 2,
                },
                {
                    "fret": 2,
                    "string": 3,
                },
                {
                    "fret": 3,
                    "string": 4,
                },
                {
                    "fret": 3,
                    "string": 5,
                },
                {
                    "fret": 1,
                    "string": 6,
                },
            ],
            "gb": [
                {
                    "fret": 2,
                    "string": 1,
                },
                {
                    "fret": 2,
                    "string": 2,
                },
                {
                    "fret": 3,
                    "string": 3,
                },
                {
                    "fret": 4,
                    "string": 4,
                },
                {
                    "fret": 4,
                    "string": 5,
                },
                {
                    "fret": 2,
                    "string": 6,
                },
            ],
            "g": [
                {
                    "fret": 3,
                    "string": 1,
                },
                {
                    "fret": 0,
                    "string": 2,
                },
                {
                    "fret": 0,
                    "string": 3,
                },
                {
                    "fret": 0,
                    "string": 4,
                },
                {
                    "fret": 2,
                    "string": 5,
                },
                {
                    "fret": 3,
                    "string": 6,
                },
            ],
        },
        "ukulele": {
            "ab": [
                {
                    "fret": 3,
                    "string": 1,
                },
                {
                    "fret": 4,
                    "string": 2,
                },
                {
                    "fret": 3,
                    "string": 3,
                },
                {
                    "fret": 1,
                    "string": 4,
                },
            ],
            "a": [
                {
                    "fret": 0,
                    "string": 1,
                },
                {
                    "fret": 0,
                    "string": 2,
                },
                {
                    "fret": 1,
                    "string": 3,
                },
                {
                    "fret": 2,
                    "string": 4,
                },
            ],
            "bb": [
                {
                    "fret": 1,
                    "string": 1,
                },
                {
                    "fret": 1,
                    "string": 2,
                },
                {
                    "fret": 2,
                    "string": 3,
                },
                {
                    "fret": 3,
                    "string": 4,
                },
            ],
            "b": [
                {
                    "fret": 2,
                    "string": 1,
                },
                {
                    "fret": 2,
                    "string": 2,
                },
                {
                    "fret": 3,
                    "string": 3,
                },
                {
                    "fret": 4,
                    "string": 4,
                },
            ],
            "c": [
                {
                    "fret": 3,
                    "string": 1,
                },
                {
                    "fret": 0,
                    "string": 2,
                },
                {
                    "fret": 0,
                    "string": 3,
                },
                {
                    "fret": 0,
                    "string": 4,
                },
            ],
            "db": [
                {
                    "fret": 4,
                    "string": 1,
                },
                {
                    "fret": 1,
                    "string": 2,
                },
                {
                    "fret": 1,
                    "string": 3,
                },
                {
                    "fret": 1,
                    "string": 4,
                },
            ],
            "d": [
                {
                    "fret": 0,
                    "string": 1,
                },
                {
                    "fret": 2,
                    "string": 2,
                },
                {
                    "fret": 2,
                    "string": 3,
                },
                {
                    "fret": 2,
                    "string": 4,
                },
            ],
            "eb": [
                {
                    "fret": 1,
                    "string": 1,
                },
                {
                    "fret": 3,
                    "string": 2,
                },
                {
                    "fret": 3,
                    "string": 3,
                },
                {
                    "fret": 0,
                    "string": 4,
                },
            ],
            "e": [
                {
                    "fret": 2,
                    "string": 1,
                },
                {
                    "fret": 4,
                    "string": 2,
                },
                {
                    "fret": 4,
                    "string": 3,
                },
                {
                    "fret": 4,
                    "string": 4,
                },
            ],
            "f": [
                {
                    "fret": 0,
                    "string": 1,
                },
                {
                    "fret": 1,
                    "string": 2,
                },
                {
                    "fret": 0,
                    "string": 3,
                },
                {
                    "fret": 2,
                    "string": 4,
                },
            ],
            "gb": [
                {
                    "fret": 1,
                    "string": 1,
                },
                {
                    "fret": 2,
                    "string": 2,
                },
                {
                    "fret": 1,
                    "string": 3,
                },
                {
                    "fret": 3,
                    "string": 4,
                },
            ],
            "g": [
                {
                    "fret": 2,
                    "string": 1,
                },
                {
                    "fret": 3,
                    "string": 2,
                },
                {
                    "fret": 2,
                    "string": 3,
                },
                {
                    "fret": 0,
                    "string": 4,
                },
            ],
        }
    }
    }
  },
  methods: {
    handler (name, note) {
      this.getChord(note)
      this.note = note
      this.chordName = name
    },
    changeInstrument (instrument) {
      this.instrument = instrument
      this.getChord(this.note)
    },
    playChord (chord, duration = 500) {
      let sampler = new Tone.Sampler(this.samplers.piano, {
        baseUrl: '/static/audio/piano/',
        onload: () => {
          for (var i = 0; i < chord.length; i++) {
            sampler.triggerAttackRelease(chord[i], 2)
          }
        },
        attack : 0.05
      }).toMaster();
    },
    getChord (note) {
      if (note === null) {
        return false
      }
      this.chord = this.chords[this.instrument][note.replace("#", "s").toLowerCase()]
      this.playChord(this.buildChord(this.chord))
      // const path = 'https://arpego-api.herokuapp.com/api/chord/' + this.instrument + '/'
      // axios.get(path + note.replace("#", "s").toLowerCase())
      // .then(response => {
      //   this.chord = response.data
      //   this.playChord(this.buildChord(this.chord))
      // })
      // .catch(error => {
      //   console.log(error)
      // })
    },
    showNote (fret, string) {
      for (var i = 0; i < this.chord.length; i++) { 
        if (this.chord[i]['fret'] == fret && this.chord[i]['string'] == string) {
          return true;
        }
      }
    },
    buildChord (chord) {
      var list = []
      for (var i = 0; i < chord.length; i++) {
        if (this.instrument in this.map) {
          if (chord[i]['string'] in this.map[this.instrument]) {
            if (chord[i]['fret'] in this.map[this.instrument][chord[i]['string']]) {
              list.push(this.map[this.instrument][chord[i]['string']][chord[i]['fret']])
            }
          }
        } 
      }
      return list
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