import React from 'react'
import Card from './card.js'
import { socket } from './websocket/socket.js'

export default class Field extends React.Component {
  render () {
    const hand = []
    const last = this.props.hand.slice(
      Math.max(this.props.hand.length - 5, 0)
    )
    for (const card of last) {
      hand.push(
        <Card 
          key={card.uid}
          {...card}
          rid={this.props.rid}
          onCardPlayed={this.onCardPlayed}
        />
      )
    }
    return (
      <div>{hand}</div>
    )
  }
  
}
