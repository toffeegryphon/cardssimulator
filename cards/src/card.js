import React from 'react'
import './card.css'
import { playCard } from './websocket/socket.js'

export default class Card extends React.Component {
  handleClick = (event) => {
    playCard(this.props.uid, this.props.rid, this.props.onCardPlayed)
  }

  render() {
    return (
      <div className='card noselect' onClick={this.handleClick}>
        {this.props.suit} {this.props.value}
      </div>
    )
  }
}
