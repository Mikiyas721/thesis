module.exports = function(Model, bootOptions) {
  const options = Object.assign({
    createdAt: 'createdAt',
    required: false,
    validateUpsert: false, // default to turning validation off
    silenceWarnings: false,
    index: false,
  }, bootOptions);

  Model.defineProperty(options.createdAt, {
    type: Date,
    required: options.required,
    defaultFn: 'now',
    index: options.index,
  });

};
