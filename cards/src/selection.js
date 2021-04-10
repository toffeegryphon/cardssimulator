import React from 'react';
import { joinRoom } from './websocket/socket.js'

export default class Selection extends React.Component {
  constructor(props) {
    super(props)
    this.state = { rid: '' }
  }

  setRid = (rid) => {
    this.setState({ rid })
    console.log(rid)
  }

  handleChange = (event) => {
    this.setRid(event.target.value)
  }

  handleJoin = (event) => {
    joinRoom(this.state.rid, this.setRid)
  }

  render() {
    return (
      <div>
        <div>Enter Room Code: </div>
        <input value={this.state.rid} onChange={this.handleChange}/>
        <button onClick={this.handleJoin}>Join</button>
      </div>
    )
  }
}
