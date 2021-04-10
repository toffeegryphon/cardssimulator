import React from 'react';
import { joinRoom } from './websocket/socket.js'

export default class Selection extends React.Component {
  constructor(props) {
    super(props)
    this.state = { rid: '', joined: false }
  }

  onJoined = (rid) => {
    this.setState({ rid, joined: true })
  }

  handleChange = (event) => {
    this.setState({ rid: event.target.value })
  }

  handleJoin = (event) => {
    joinRoom(this.state.rid, this.onJoined)
  }

  render() {
    if (this.state.joined) {
      return (
        <div>Room {this.state.rid}</div>
      )
    }
    return (
      <div>
        <div>Enter Room Code: </div>
        <input value={this.state.rid} onChange={this.handleChange}/>
        <button onClick={this.handleJoin}>Join</button>
      </div>
    )
  }
}
