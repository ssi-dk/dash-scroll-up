import React from 'react';
import {shallow} from 'enzyme';
import DashScrollUp from '../DashScrollUp.react';

describe('ExampleComponent', () => {

    it('renders', () => {
        const component = shallow(<DashScrollUp label="Test label"/>);
        expect(component).to.be.ok;
    });
});
