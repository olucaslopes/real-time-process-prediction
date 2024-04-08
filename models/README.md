# Models

## v1.0.0

**Features:**

- `vazaoVapor`
- `pressaoVapor`
- `temperaturaVapor`
- `cargaVaporTG1`
- `cargaVaporTG2`
- `habilitaTG1`
- `habilitaTG2`

**Targets:** 

- `consumoEspecificoTG1_1`
- `consumoEspecificoTG1_2`
- `consumoEspecificoTG2_1`
- `consumoEspecificoTG2_2`
- `potenciaGeradaTG1_1`
- `potenciaGeradaTG1_2`
- `potenciaGeradaTG2_1`
- `potenciaGeradaTG2_2`
- `vazaoVaporEscape`
- `pressaoVaporEscape`
- `temperaturaVaporEscape`

**Code:**

```python

    model = Sequential()

    model.add(Input(shape=(len(features),)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(targets)))

    model.compile(optimizer='adam', loss='mean_squared_error')

    early_stopping_cb = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    model_checkpoint_cb = ModelCheckpoint('./models/dense_64_32_11_mse.keras', monitor='val_loss', save_best_only=True, verbose=1)

    set_random_seed(42)
    model.fit(X_train, y_train, epochs=1000, validation_data=(X_val, y_val), callbacks=[early_stopping_cb, model_checkpoint_cb])

```

## v2.0.0

**Features:**

Same as v1.0.0

**Targets:**

All features from v1.0.0 except:
- `temperaturaVaporEscape`
- `pressaoVaporEscape`

**Code:**

Same as v1.0.0

**Changes:**
- Remove two targets because they are constant and only add noise to the model.
- Apparently there was a mistake in the train_test_split, which caused the first model to be trained only in a small portion of the data. This model was trained with the correct split.

