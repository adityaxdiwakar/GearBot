import {Component, h} from "preact";

import {GearProps} from "./props";
import {GearState} from "./state";

export default class Gear extends Component<GearProps, GearState> {

	render() {
		return (
			<div class="gearContainer" style={"width:" + this.props.size + "px;height:" + this.props.size + "px;"} >
				<img class="gear" src="/assets/gear.svg" style={"transform:rotate(" + this.state.rotation + "deg);"} />
				{this.props.image ? <img class="gearImage" src={this.props.image} /> : null}
			</div>
		);
	}
}
