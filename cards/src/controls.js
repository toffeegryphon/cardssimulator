import React from 'react'
import { drawCards, dealCards } from './websocket/socket.js'

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

  handleDraw = (event) => {
    drawCards(this.state.drawCount, this.props.rid, this.props.onDraw)
  }

  handleDeal = (event) => {
    dealCards(this.state.dealCount, this.props.rid)
  }

  render() {
    return (
      <div>
        <div>
        <button onClick={this.handleDraw}>Draw</button>
          <input
            type="number"
            value={this.state.drawCount}
            onChange={this.handleChangeDraw}
          />
        </div>
        <div>
          <button onClick={this.handleDeal}>Deal</button>
          <input type="number"
            value={this.state.dealCount}
            onChange={this.handleChangeDeal}/>
        </div>
      </div>
    )
  }
}
