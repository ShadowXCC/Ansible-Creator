import React from 'react';

export default function MessageView2() {
  return (
    <div className="message">
      <div className="field">
        <span className="label">From: </span>
        <span className="value">John Doe</span>
      </div>
      <div className="field">
        <span className="label">Status: </span>
        <span className="value"> Unread</span>
      </div>
      <div className="field content">
        <span className="label">Message: </span>
        <span className="value">Have a great day!</span>
      </div>
    </div>
  );
}