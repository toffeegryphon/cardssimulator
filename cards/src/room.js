import React from 'react'
import './room.css'
import Field from './field.js'
import Card from './card.js'
import Controls from './controls.js'
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
      ],
      field: []
    }
  }

  componentDidMount() {
    socket.on('update', (data) => {
      console.log(data)
      if (data.target === '_field') {
        this.setState({ field: this.state.field.concat(data.value) })
      } else if (data.action === 'add') {
        this.setState({ hand: this.state.hand.concat(data.value) })
      }
    })
  }

  onUpdate = (response) => {
    console.log(response)
    if (response.action === 'remove') {
      this.setState({ hand: this.state.hand.filter((card) => {
        return !response.value.includes(card.uid) 
      })})
    } else if (response.action === 'add') {
      console.log(response.value)
      this.setState({ hand: this.state.hand.concat(response.value) })
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
          onCardPlayed={this.onUpdate}
        />
      )
    }

    return (
      <div>
        <Field hand={this.state.field}/>
        <div className="hand">
          {hand}
        </div>
        <Controls 
          rid={this.props.rid} 
          onDraw={this.onUpdate} />
      </div>
    )
  }
}
