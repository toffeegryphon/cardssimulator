import React from 'react'
import './room.css'
import Field from './field.js'
import Card from './card.js'
import Controls from './controls.js'
import Players from './players.js'
import { socket } from './websocket/socket.js'

export default class Room extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      _deckSize: 0,
      _players: {},
      hand: [],
      field: []
    }
  }

  componentDidMount() {
    socket.on('update', (data) => {
      console.log(data)
      const newState = {
        _deckSize: data.state._deck
      }
      delete data.state._deck
      delete data.state._field
      delete data.state[this.props.sid]
      newState['_players'] = data.state

      if (data.target === '_field') {
        newState['field'] = this.state.field.concat(data.value)
        // this.setState({ field: this.state.field.concat(data.value) })
      } else if (data.action === 'add') {
        newState['hand'] = this.state.hand.concat(data.value)
        // this.setState({ hand: this.state.hand.concat(data.value) })
      }
      this.setState(newState)
    })
  }

  onUpdate = (response) => {
    console.log(response)
    if (response.action === 'remove') {
      const uids = response.value.map(card => card.uid);
      this.setState({ hand: this.state.hand.filter((card) => {
        return !uids.includes(card.uid) 
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
        <Players players={this.state._players}/>
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
