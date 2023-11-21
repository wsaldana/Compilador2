import './App.css';
import { Button, TextareaAutosize } from '@mui/material';
import { useState } from 'react';

function App() {

  const [err, setErr] = useState(false);
  const [output, setOutput] = useState('');
  const [symtab, setSymtab] = useState('');
  const [typing, setTyping] = useState('');
  const [tac, setTac] = useState('');
  const [mips, setMips] = useState('');
  const [scriptCode, setScriptCode] = useState('');

  const runPythonScript = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/run-python-script', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ script_code: scriptCode }),
      });

      if (response.ok) {
        const data = await response.json();
        if (data.error) {
          setErr(true)
          setOutput(data.error);
          setSymtab('')
          setTyping('')
          setTac('')
          setMips('')
        } else {
          setErr(false)
          console.log(data)
          setOutput(data.output);
          setSymtab(data.symtab)
          setTyping(data.typing)
          setTac(data.tac)
          setMips(data.mips)
        }
      } else {
        console.error('Error running the Python script.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <div className="gjs-row" id="ifof">
        <div className="gjs-cell" id="ibar">
          <div className="gjs-row" id="i4sn">
            <div className="gjs-cell" id="imiz">
              <TextareaAutosize
                id="ix74c"
                placeholder='Insert code...'
                value={scriptCode}
                onChange={(e) => setScriptCode(e.target.value)}
              />
            </div>
            <div className="gjs-cell" id="iyad"><img id="in3qx" alt='tree'
                src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIHZpZXdCb3g9IjAgMCAyNCAyNCIgc3R5bGU9ImZpbGw6IHJnYmEoMCwwLDAsMC4xNSk7IHRyYW5zZm9ybTogc2NhbGUoMC43NSkiPgogICAgICAgIDxwYXRoIGQ9Ik04LjUgMTMuNWwyLjUgMyAzLjUtNC41IDQuNSA2SDVtMTYgMVY1YTIgMiAwIDAgMC0yLTJINWMtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxNGMxLjEgMCAyLS45IDItMnoiPjwvcGF0aD4KICAgICAgPC9zdmc+" />
            </div>
          </div>
          <div className="gjs-row" id="irsl4">
            <div className="gjs-cell" id="isiwj">
              <Button
                id="ibyt"
                onClick={runPythonScript}
              >
                RUN<br />
              </Button>
            </div>
          </div>
          <div className="gjs-col" id="iv4d">
            <div className="gjs-cell" id="iqlk">
              <div id="i4fwu" style={err ? {color: 'red'} : {color: 'lime'}}>{output ? output : "Output:"}<br /></div>
            </div>
            <br></br>
            <div className="gjs-cell" id="iqlk">
              <div id="i4fwu">{symtab ? symtab : "Symtab:"}<br /></div>
            </div>
            <br></br>
            <div className="gjs-cell" id="iqlk">
              <div id="i4fwu" style={typing ? {color: 'red'} : {color: 'lime'}}>
                {typing ? typing : "No typing errors"}<br />
              </div>
            </div>
            <br></br>
            <div className="gjs-cell" id="iqlk">
              <div id="i4fwu1" style={typing ? {color: 'red'} : {color: 'lime'}}>
                {tac ? tac : "TAC:"}<br />
              </div>
            </div>
            <br></br>
            <div className="gjs-cell" id="iqlk">
              <div id="i4fwu1" style={typing ? {color: 'red'} : {color: 'lime'}}>
                {mips ? mips : "MIPS:"}<br />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
