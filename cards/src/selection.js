import React from 'react'
import Room from './room.js'
import { joinRoom } from './websocket/socket.js'

export default class Selection extends React.Component {
  constructor(props) {
    super(props)
    this.state = { rid: '', sid: '', joined: false }
  }

  onJoined = (data) => {
    this.setState({ ...data, joined: true })
  }

  handleChange = (event) => {
    this.setState({ rid: event.target.value })
  }

  handleJoin = (event) => {
    // TODO Change to an input field
    joinRoom('testing', this.state.rid, this.onJoined)
  }

  render() {
    if (this.state.joined) {
      return (
        <div>
          <div>Room {this.state.rid}</div>
          <Room rid={this.state.rid} sid={this.state.sid}/>
        </div>
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
