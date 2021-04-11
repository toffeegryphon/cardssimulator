import React from 'react'
import { initialize, drawCards, dealCards } from './websocket/socket.js'
import './controls.css'

export default class Controls extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      drawCount: 1,
      dealCount: 5
    }
  }

  handleChangeDraw = (event) => {
    this.setState({ drawCount: event.target.value })
  }

  handleChangeDeal = (event) => {
    this.setState({ dealCount: event.target.value })
  }

  handleInitialize = (event) => {
    initialize(this.props.rid)
  }

  handleDraw = (event) => {
    drawCards(this.state.drawCount, this.props.rid, this.props.onDraw)
  }

  handleDeal = (event) => {
    dealCards(this.state.dealCount, this.props.rid)
  }

  render() {
    return (
      <div className="controls">
        <div className="control">
          <button onClick={this.handleInitialize}>Start</button>
        </div>
        <div className="control">
          <button onClick={this.handleDraw}>Draw</button>
          <input
            type="number" min="0" max="52"
            value={this.state.drawCount}
            onChange={this.handleChangeDraw}
          />
        </div>
        <div className="control">
          <button onClick={this.handleDeal}>Deal</button>
          <input type="number" min="0" max="52"
            value={this.state.dealCount}
            onChange={this.handleChangeDeal}/>
        </div>
        <div className="info">Only one player presses start when 
      everyone is ready! That will automatically shuffle the deck. 
      Deal deals to everyone, draw only draws to yourself.</div>
      </div>
    )
  }
}
