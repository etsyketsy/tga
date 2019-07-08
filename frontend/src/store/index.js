import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

import masterReducer from './reducers/master_reducer.js';


const store = createStore(masterReducer, applyMiddleware(thunk));

export default store;
