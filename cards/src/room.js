import React from 'react'
import './room.css'
import Field from './field.js'
import Card from './card.js'
import Controls from './controls.js'
import Players from './players.js'
import { socket, requestState } from './websocket/socket.js'

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
    requestState(this.props.rid, this.onUpdate)
    socket.on('update', (data) => {
      this.onUpdate(data)
      // console.log(data)
      // const newState = {
        // _deckSize: data.state._deck
      // }
      // delete data.state._deck
      // delete data.state._field
      // delete data.state[this.props.sid]
      // newState['_players'] = data.state
      // if (data.target === '_field') {
        // newState['field'] = this.state.field.concat(data.value)
      // } else if (data.action === 'add') {
        // newState['hand'] = this.state.hand.concat(data.value)
      // } else if (response.action === 'remove') {
        // const uids = response.value.map(card => card.uid);
        // newState['hand'] = this.state.hand.filter((card) => {
          // return !uids.includes(card.uid)
        // })
      // }
      // this.setState(newState)
    })
  }

  onUpdate = (response) => {
    console.log(response)
    const newState = {
    }
    if ('state' in response) {
      newState['_deckSize'] = response.state._deck
      delete response.state._deck
      delete response.state._field
      delete response.state[this.props.sid]
      newState['_players'] = response.state
    }

    if (response.target === '_field') {
      newState['field'] = this.state.field.concat(response.value)
      // this.setState({ field: this.state.field.concat(data.value) })
    } else if (response.action === 'add') {
      newState['hand'] = this.state.hand.concat(response.value)
      // this.setState({ hand: this.state.hand.concat(data.value) })
    } else if (response.action === 'remove') {
      const uids = response.value.map(card => card.uid);
      newState['hand'] = this.state.hand.filter((card) => {
        return !uids.includes(card.uid) 
      })
    }
    this.setState(newState)
  }

  // onUpdate = (response) => {
    // console.log(response)
    // if (response.action === 'remove') {
      // const uids = response.value.map(card => card.uid);
      // this.setState({ hand: this.state.hand.filter((card) => {
        // return !uids.includes(card.uid)
      // })})
    // } else if (response.action === 'add') {
      // console.log(response.value)
      // this.setState({ hand: this.state.hand.concat(response.value) })
    // }
  // }

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
      <div className="room">
        <Players players={this.state._players}/>
        <Field hand={this.state.field}/>
        <div className="hand">
          <div className="watermark noselect">HAND</div>
          {hand}
        </div>
        <Controls 
          rid={this.props.rid} 
          onDraw={this.onUpdate} />
      </div>
    )
  }
}
