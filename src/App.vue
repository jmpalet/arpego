<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
* { box-sizing:border-box; }
body{ margin:0; min-width: 610px; }
ul.set {
	height:18.875em; width:34em;
  margin:2em auto; padding:3em 0 0 3em; position:relative; 
  border:1px solid #160801; border-radius:1em;
  background: #222;
}
li { margin:0; padding:0; list-style:none; position:relative; float:left; }
ul.set .white {
	height:16em; width:4em; z-index:1;
	border-left:1px solid #bbb;
	border-bottom:1px solid #bbb;
	border-radius:0 0 5px 5px;
	box-shadow:-1px 0 0 rgba(255,255,255,0.8) inset, 0 0 5px #ccc inset, 0 0 3px rgba(0,0,0,0.2);
	background: white;
}
ul.set .white:active {
	border-top:1px solid #777;
	border-left:1px solid #999;
	border-bottom:1px solid #999;
	box-shadow:2px 0 3px rgba(0,0,0,0.1) inset, -5px 5px 20px rgba(0,0,0,0.2) inset,0 0 3px rgba(0,0,0,0.2);
	background: linear-gradient(top, #fff 0%,#e9e9e9 100%);
}
.black {
	height:8em; width:2em; margin:0 0 0 -1em; z-index:2;
	border:1px solid #000;
	border-radius:0 0 3px 3px;
	box-shadow:-1px -1px 2px rgba(255,255,255,0.2) inset, 0 -5px 2px 3px rgba(0,0,0,0.6) inset, 0 2px 4px rgba(0,0,0,0.5);
	background:linear-gradient(45deg, #222 0%,#555 100%);
}
.black:active {
	box-shadow:-1px -1px 2px rgba(255,255,255,0.2) inset, 0 -2px 2px 3px rgba(0,0,0,0.6) inset, 0 1px 2px rgba(0,0,0,0.5);
	background:linear-gradient(left, #444 0%,#222 100%);
}
.d,.e,.g,.a,.b { margin:0 0 0 -1em;  }
ul.set li:first-child { border-radius:5px 0 5px 5px; }
ul.set li:last-child { border-radius:0 5px 5px 5px; }
.chordname {
  font-size: 2rem;
  font-weight: bold;
  text-align: center;
  position: relative;
  margin-left: -19px;
}
.diagram .strings {
  width: 610px;
  margin: 0 auto;
}
.diagram .row {
  clear: both;
}
.diagram .row.first .fret {
  border-top: 1px solid #222;
}
.diagram .row.last .fret {
  border: 0;
}
.diagram .cell {
  float: left;
  position: relative;
  width: 76px;
  height: 32px;
}
.diagram .cell.fret {
  border: 1px solid #222;
  border-top: 0;
}
.diagram .cell.fret:first-of-type {
  border-left: 3px solid #222;
}
.diagram .row.last .cell.fret:first-of-type {
  border: 0;
}
.diagram .cell.fret:not(:last-of-type) {
  border-right: 0;
}
.diagram .cell .note {
  position: absolute;
  z-index: 2;
  width: 26px;
  height: 26px;
  left: 50%;
  margin-left: -13px;
  margin-top: -13px;
  color: #fff;
  background: #222;
  text-align: center;
  border-radius: 50%;
  padding-top: 4px;
  
}
.choice-list {
  margin-bottom: 1em;
}
button.choice {
  outline: none;
  color: #777;
  background: transparent;
  border: 0;
  text-transform: uppercase;
  font-weight: bold;
}
button.choice.active, button.choice:hover {
  color: #222;
  border-bottom: 2px solid #222
}
</style>