import React from 'react'
import Room from './room.js'
import { joinRoom } from './websocket/socket.js'
import './selection.css'

export default class Selection extends React.Component {
  constructor(props) {
    super(props)
    this.state = { rid: '', sid: '', name: '', joined: false }
  }

  onJoined = (data) => {
    this.setState({ ...data, joined: true })
  }

  handleRidChange = (event) => {
    this.setState({ rid: event.target.value })
  }

  handleNameChange = (event)=> {
    this.setState({ name: event.target.value })
  }

  handleJoin = (event) => {
    // TODO Change to an input field
    joinRoom(this.state.name, this.state.rid, this.onJoined)
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
      <div className="selection">
        <div>ROOM CODE</div>
        <input value={this.state.rid} onChange={this.handleRidChange}/>
        <br/>
        <br/>
        <div>DISPLAY NAME</div>
        <input value={this.state.name} onChange={this.handleNameChange}/>
        <br/>
        <br/>
        <button onClick={this.handleJoin}>Join</button>
      </div>
    )
  }
}
