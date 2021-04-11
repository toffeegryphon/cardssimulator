import React from 'react'
import './players.css'

export default class Players extends React.Component {
  render() {
    const players = []
    for (const [sid, player] of Object.entries(this.props.players)) {
      players.push(
        <div className="player" key={sid}>
          <div className="name">{player.name}</div>
          <div className="count">{player.count}</div>
        </div>
      )
    }
    return (
      <div className="players">{players}</div>
    )
  }
}
