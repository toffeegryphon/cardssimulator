import React from 'react'
import './room.css'
import Card from './card.js'
import { socket } from './websocket/socket.js'

export default class Room extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      _deckSize: 0,
      _players: {},
      hand: [
        { uid: 12, suit: 'Spades', value: 'King' },
        { uid: 15, suit: 'Hearts', value: '3' }
      ]
    }
  }

  onCardPlayed = (response) => {
    console.log(response)
    if (response.action === 'remove') {
      this.setState({ hand: this.state.hand.filter((card) => {
        return !response.value.includes(card.uid) })
      })
    }
  }

  render () {
    const hand = []
    for (const card of this.state.hand) {
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
      <div className="hand">
        {hand}
      </div>
    )
  }
}
