# luisd.model.basket_identifier.BasketIdentifier

Descriptive information that describes a particular basket of instruments. Most commonly required with a CDS Index or similarly defined instrument.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Descriptive information that describes a particular basket of instruments. Most commonly required with a CDS Index or similarly defined instrument. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The index name within the set, e.g. \&quot;MAIN\&quot; or \&quot;Crossover\&quot;. | 
**index** | str,  | str,  | Index set, e.g. iTraxx or CDX. | 
**region** | str,  | str,  | Applicable geographic country or region. Typically something like \&quot;Europe\&quot;, \&quot;Asia ex-Japan\&quot;, \&quot;Japan\&quot; or \&quot;Australia\&quot;. | 
**seriesId** | decimal.Decimal, int,  | decimal.Decimal,  | The series identifier. | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

