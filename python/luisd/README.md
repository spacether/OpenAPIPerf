# luisd
# Introduction

This page documents the [LUSID APIs](https://www.lusid.com/api/swagger), which allows authorised clients to query and update their data within the LUSID platform.

SDKs to interact with the LUSID APIs are available in the following languages and frameworks:

* [C#](https://github.com/finbourne/lusid-sdk-csharp)
* [Java](https://github.com/finbourne/lusid-sdk-java)
* [JavaScript](https://github.com/finbourne/lusid-sdk-js)
* [Python](https://github.com/finbourne/lusid-sdk-python)
* [Angular](https://github.com/finbourne/lusid-sdk-angular)

The LUSID platform is made up of a number of sub-applications. You can find the API / swagger documentation by following the links in the table below.


| Application | Description | API / Swagger Documentation |
| ----- | ----- | ---- |
| LUSID | Open, API-first, developer-friendly investment data platform. | [Swagger](https://www.lusid.com/api/swagger/index.html) |
| Web app | User-facing front end for LUSID. | [Swagger](https://www.lusid.com/app/swagger/index.html) |
| Scheduler | Automated job scheduler. | [Swagger](https://www.lusid.com/scheduler2/swagger/index.html) |
| Insights |Monitoring and troubleshooting service. | [Swagger](https://www.lusid.com/insights/swagger/index.html) |
| Identity | Identity management for LUSID (in conjuction with Access) | [Swagger](https://www.lusid.com/identity/swagger/index.html) |
| Access | Access control for LUSID (in conjunction with Identity) | [Swagger](https://www.lusid.com/access/swagger/index.html) |
| Drive | Secure file repository and manager for collaboration. | [Swagger](https://www.lusid.com/drive/swagger/index.html) |
| Luminesce | Data virtualisation service (query data from multiple providers, including LUSID) | [Swagger](https://www.lusid.com/honeycomb/swagger/index.html) |
| Notification | Notification service. | [Swagger](https://www.lusid.com/notifications/swagger/index.html) |
| Configuration | File store for secrets and other sensitive information. | [Swagger](https://www.lusid.com/configuration/swagger/index.html) |


# Error Codes

| Code|Name|Description |
| ---|---|--- |
| <a name=\"-10\">-10</a>|Server Configuration Error|  |
| <a name=\"-1\">-1</a>|Unknown error|An unexpected error was encountered on our side. |
| <a name=\"102\">102</a>|Version Not Found|  |
| <a name=\"103\">103</a>|Api Rate Limit Violation|  |
| <a name=\"104\">104</a>|Instrument Not Found|  |
| <a name=\"105\">105</a>|Property Not Found|  |
| <a name=\"106\">106</a>|Portfolio Recursion Depth|  |
| <a name=\"108\">108</a>|Group Not Found|  |
| <a name=\"109\">109</a>|Portfolio Not Found|  |
| <a name=\"110\">110</a>|Property Schema Not Found|  |
| <a name=\"111\">111</a>|Portfolio Ancestry Not Found|  |
| <a name=\"112\">112</a>|Portfolio With Id Already Exists|  |
| <a name=\"113\">113</a>|Orphaned Portfolio|  |
| <a name=\"119\">119</a>|Missing Base Claims|  |
| <a name=\"121\">121</a>|Property Not Defined|  |
| <a name=\"122\">122</a>|Cannot Delete System Property|  |
| <a name=\"123\">123</a>|Cannot Modify Immutable Property Field|  |
| <a name=\"124\">124</a>|Property Already Exists|  |
| <a name=\"125\">125</a>|Invalid Property Life Time|  |
| <a name=\"126\">126</a>|Property Constraint Style Excludes Properties|  |
| <a name=\"127\">127</a>|Cannot Modify Default Data Type|  |
| <a name=\"128\">128</a>|Group Already Exists|  |
| <a name=\"129\">129</a>|No Such Data Type|  |
| <a name=\"130\">130</a>|Undefined Value For Data Type|  |
| <a name=\"131\">131</a>|Unsupported Value Type Defined On Data Type|  |
| <a name=\"132\">132</a>|Validation Error|  |
| <a name=\"133\">133</a>|Loop Detected In Group Hierarchy|  |
| <a name=\"134\">134</a>|Undefined Acceptable Values|  |
| <a name=\"135\">135</a>|Sub Group Already Exists|  |
| <a name=\"138\">138</a>|Price Source Not Found|  |
| <a name=\"139\">139</a>|Analytic Store Not Found|  |
| <a name=\"141\">141</a>|Analytic Store Already Exists|  |
| <a name=\"143\">143</a>|Client Instrument Already Exists|  |
| <a name=\"144\">144</a>|Duplicate In Parameter Set|  |
| <a name=\"147\">147</a>|Results Not Found|  |
| <a name=\"148\">148</a>|Order Field Not In Result Set|  |
| <a name=\"149\">149</a>|Operation Failed|  |
| <a name=\"150\">150</a>|Elastic Search Error|  |
| <a name=\"151\">151</a>|Invalid Parameter Value|  |
| <a name=\"153\">153</a>|Command Processing Failure|  |
| <a name=\"154\">154</a>|Entity State Construction Failure|  |
| <a name=\"155\">155</a>|Entity Timeline Does Not Exist|  |
| <a name=\"156\">156</a>|Concurrency Conflict Failure|  |
| <a name=\"157\">157</a>|Invalid Request|  |
| <a name=\"158\">158</a>|Event Publish Unknown|  |
| <a name=\"159\">159</a>|Event Query Failure|  |
| <a name=\"160\">160</a>|Blob Did Not Exist|  |
| <a name=\"162\">162</a>|Sub System Request Failure|  |
| <a name=\"163\">163</a>|Sub System Configuration Failure|  |
| <a name=\"165\">165</a>|Failed To Delete|  |
| <a name=\"166\">166</a>|Upsert Client Instrument Failure|  |
| <a name=\"167\">167</a>|Illegal As At Interval|  |
| <a name=\"168\">168</a>|Illegal Bitemporal Query|  |
| <a name=\"169\">169</a>|Invalid Alternate Id|  |
| <a name=\"170\">170</a>|Cannot Add Source Portfolio Property Explicitly|  |
| <a name=\"171\">171</a>|Entity Already Exists In Group|  |
| <a name=\"173\">173</a>|Entity With Id Already Exists|  |
| <a name=\"174\">174</a>|Derived Portfolio Details Do Not Exist|  |
| <a name=\"176\">176</a>|Portfolio With Name Already Exists|  |
| <a name=\"177\">177</a>|Invalid Transactions|  |
| <a name=\"178\">178</a>|Reference Portfolio Not Found|  |
| <a name=\"179\">179</a>|Duplicate Id|  |
| <a name=\"180\">180</a>|Command Retrieval Failure|  |
| <a name=\"181\">181</a>|Data Filter Application Failure|  |
| <a name=\"182\">182</a>|Search Failed|  |
| <a name=\"183\">183</a>|Movements Engine Configuration Key Failure|  |
| <a name=\"184\">184</a>|Fx Rate Source Not Found|  |
| <a name=\"185\">185</a>|Accrual Source Not Found|  |
| <a name=\"186\">186</a>|Access Denied|  |
| <a name=\"187\">187</a>|Invalid Identity Token|  |
| <a name=\"188\">188</a>|Invalid Request Headers|  |
| <a name=\"189\">189</a>|Price Not Found|  |
| <a name=\"190\">190</a>|Invalid Sub Holding Keys Provided|  |
| <a name=\"191\">191</a>|Duplicate Sub Holding Keys Provided|  |
| <a name=\"192\">192</a>|Cut Definition Not Found|  |
| <a name=\"193\">193</a>|Cut Definition Invalid|  |
| <a name=\"194\">194</a>|Time Variant Property Deletion Date Unspecified|  |
| <a name=\"195\">195</a>|Perpetual Property Deletion Date Specified|  |
| <a name=\"196\">196</a>|Time Variant Property Upsert Date Unspecified|  |
| <a name=\"197\">197</a>|Perpetual Property Upsert Date Specified|  |
| <a name=\"200\">200</a>|Invalid Unit For Data Type|  |
| <a name=\"201\">201</a>|Invalid Type For Data Type|  |
| <a name=\"202\">202</a>|Invalid Value For Data Type|  |
| <a name=\"203\">203</a>|Unit Not Defined For Data Type|  |
| <a name=\"204\">204</a>|Units Not Supported On Data Type|  |
| <a name=\"205\">205</a>|Cannot Specify Units On Data Type|  |
| <a name=\"206\">206</a>|Unit Schema Inconsistent With Data Type|  |
| <a name=\"207\">207</a>|Unit Definition Not Specified|  |
| <a name=\"208\">208</a>|Duplicate Unit Definitions Specified|  |
| <a name=\"209\">209</a>|Invalid Units Definition|  |
| <a name=\"210\">210</a>|Invalid Instrument Identifier Unit|  |
| <a name=\"211\">211</a>|Holdings Adjustment Does Not Exist|  |
| <a name=\"212\">212</a>|Could Not Build Excel Url|  |
| <a name=\"213\">213</a>|Could Not Get Excel Version|  |
| <a name=\"214\">214</a>|Instrument By Code Not Found|  |
| <a name=\"215\">215</a>|Entity Schema Does Not Exist|  |
| <a name=\"216\">216</a>|Feature Not Supported On Portfolio Type|  |
| <a name=\"217\">217</a>|Quote Not Found|  |
| <a name=\"218\">218</a>|Invalid Quote Identifier|  |
| <a name=\"219\">219</a>|Invalid Metric For Data Type|  |
| <a name=\"220\">220</a>|Invalid Instrument Definition|  |
| <a name=\"221\">221</a>|Instrument Upsert Failure|  |
| <a name=\"222\">222</a>|Reference Portfolio Request Not Supported|  |
| <a name=\"223\">223</a>|Transaction Portfolio Request Not Supported|  |
| <a name=\"224\">224</a>|Invalid Property Value Assignment|  |
| <a name=\"230\">230</a>|Transaction Type Not Found|  |
| <a name=\"231\">231</a>|Transaction Type Duplication|  |
| <a name=\"232\">232</a>|Portfolio Does Not Exist At Given Date|  |
| <a name=\"233\">233</a>|Query Parser Failure|  |
| <a name=\"234\">234</a>|Duplicate Constituent|  |
| <a name=\"235\">235</a>|Unresolved Instrument Constituent|  |
| <a name=\"236\">236</a>|Unresolved Instrument In Transition|  |
| <a name=\"237\">237</a>|Missing Side Definitions|  |
| <a name=\"299\">299</a>|Invalid Recipe|  |
| <a name=\"300\">300</a>|Missing Recipe|  |
| <a name=\"301\">301</a>|Dependencies|  |
| <a name=\"304\">304</a>|Portfolio Preprocess Failure|  |
| <a name=\"310\">310</a>|Valuation Engine Failure|  |
| <a name=\"311\">311</a>|Task Factory Failure|  |
| <a name=\"312\">312</a>|Task Evaluation Failure|  |
| <a name=\"313\">313</a>|Task Generation Failure|  |
| <a name=\"314\">314</a>|Engine Configuration Failure|  |
| <a name=\"315\">315</a>|Model Specification Failure|  |
| <a name=\"320\">320</a>|Market Data Key Failure|  |
| <a name=\"321\">321</a>|Market Resolver Failure|  |
| <a name=\"322\">322</a>|Market Data Failure|  |
| <a name=\"330\">330</a>|Curve Failure|  |
| <a name=\"331\">331</a>|Volatility Surface Failure|  |
| <a name=\"332\">332</a>|Volatility Cube Failure|  |
| <a name=\"350\">350</a>|Instrument Failure|  |
| <a name=\"351\">351</a>|Cash Flows Failure|  |
| <a name=\"352\">352</a>|Reference Data Failure|  |
| <a name=\"360\">360</a>|Aggregation Failure|  |
| <a name=\"361\">361</a>|Aggregation Measure Failure|  |
| <a name=\"370\">370</a>|Result Retrieval Failure|  |
| <a name=\"371\">371</a>|Result Processing Failure|  |
| <a name=\"372\">372</a>|Vendor Result Processing Failure|  |
| <a name=\"373\">373</a>|Vendor Result Mapping Failure|  |
| <a name=\"374\">374</a>|Vendor Library Unauthorised|  |
| <a name=\"375\">375</a>|Vendor Connectivity Error|  |
| <a name=\"376\">376</a>|Vendor Interface Error|  |
| <a name=\"377\">377</a>|Vendor Pricing Failure|  |
| <a name=\"378\">378</a>|Vendor Translation Failure|  |
| <a name=\"379\">379</a>|Vendor Key Mapping Failure|  |
| <a name=\"380\">380</a>|Vendor Reflection Failure|  |
| <a name=\"381\">381</a>|Vendor Process Failure|  |
| <a name=\"382\">382</a>|Vendor System Failure|  |
| <a name=\"390\">390</a>|Attempt To Upsert Duplicate Quotes|  |
| <a name=\"391\">391</a>|Corporate Action Source Does Not Exist|  |
| <a name=\"392\">392</a>|Corporate Action Source Already Exists|  |
| <a name=\"393\">393</a>|Instrument Identifier Already In Use|  |
| <a name=\"394\">394</a>|Properties Not Found|  |
| <a name=\"395\">395</a>|Batch Operation Aborted|  |
| <a name=\"400\">400</a>|Invalid Iso4217 Currency Code|  |
| <a name=\"401\">401</a>|Cannot Assign Instrument Identifier To Currency|  |
| <a name=\"402\">402</a>|Cannot Assign Currency Identifier To Non Currency|  |
| <a name=\"403\">403</a>|Currency Instrument Cannot Be Deleted|  |
| <a name=\"404\">404</a>|Currency Instrument Cannot Have Economic Definition|  |
| <a name=\"405\">405</a>|Currency Instrument Cannot Have Lookthrough Portfolio|  |
| <a name=\"406\">406</a>|Cannot Create Currency Instrument With Multiple Identifiers|  |
| <a name=\"407\">407</a>|Specified Currency Is Undefined|  |
| <a name=\"410\">410</a>|Index Does Not Exist|  |
| <a name=\"411\">411</a>|Sort Field Does Not Exist|  |
| <a name=\"413\">413</a>|Negative Pagination Parameters|  |
| <a name=\"414\">414</a>|Invalid Search Syntax|  |
| <a name=\"415\">415</a>|Filter Execution Timeout|  |
| <a name=\"420\">420</a>|Side Definition Inconsistent|  |
| <a name=\"450\">450</a>|Invalid Quote Access Metadata Rule|  |
| <a name=\"451\">451</a>|Access Metadata Not Found|  |
| <a name=\"452\">452</a>|Invalid Access Metadata Identifier|  |
| <a name=\"460\">460</a>|Standard Resource Not Found|  |
| <a name=\"461\">461</a>|Standard Resource Conflict|  |
| <a name=\"462\">462</a>|Calendar Not Found|  |
| <a name=\"463\">463</a>|Date In A Calendar Not Found|  |
| <a name=\"464\">464</a>|Invalid Date Source Data|  |
| <a name=\"465\">465</a>|Invalid Timezone|  |
| <a name=\"601\">601</a>|Person Identifier Already In Use|  |
| <a name=\"602\">602</a>|Person Not Found|  |
| <a name=\"603\">603</a>|Cannot Set Identifier|  |
| <a name=\"617\">617</a>|Invalid Recipe Specification In Request|  |
| <a name=\"618\">618</a>|Inline Recipe Deserialisation Failure|  |
| <a name=\"619\">619</a>|Identifier Types Not Set For Entity|  |
| <a name=\"620\">620</a>|Cannot Delete All Client Defined Identifiers|  |
| <a name=\"650\">650</a>|The Order requested was not found.|  |
| <a name=\"654\">654</a>|The Allocation requested was not found.|  |
| <a name=\"655\">655</a>|Cannot build the fx forward target with the given holdings.|  |
| <a name=\"656\">656</a>|Group does not contain expected entities.|  |
| <a name=\"665\">665</a>|Destination directory not found|  |
| <a name=\"667\">667</a>|Relation definition already exists|  |
| <a name=\"672\">672</a>|Could not retrieve file contents|  |
| <a name=\"673\">673</a>|Missing entitlements for entities in Group|  |
| <a name=\"674\">674</a>|Next Best Action not found|  |
| <a name=\"676\">676</a>|Relation definition not defined|  |
| <a name=\"677\">677</a>|Invalid entity identifier for relation|  |
| <a name=\"681\">681</a>|Sorting by specified field not supported|One or more of the provided fields to order by were either invalid or not supported. |
| <a name=\"682\">682</a>|Too many fields to sort by|The number of fields to sort the data by exceeds the number allowed by the endpoint |
| <a name=\"684\">684</a>|Sequence Not Found|  |
| <a name=\"685\">685</a>|Sequence Already Exists|  |
| <a name=\"686\">686</a>|Non-cycling sequence has been exhausted|  |
| <a name=\"687\">687</a>|Legal Entity Identifier Already In Use|  |
| <a name=\"688\">688</a>|Legal Entity Not Found|  |
| <a name=\"689\">689</a>|The supplied pagination token is invalid|  |
| <a name=\"690\">690</a>|Property Type Is Not Supported|  |
| <a name=\"691\">691</a>|Multiple Tax-lots For Currency Type Is Not Supported|  |
| <a name=\"692\">692</a>|This endpoint does not support impersonation|  |
| <a name=\"693\">693</a>|Entity type is not supported for Relationship|  |
| <a name=\"694\">694</a>|Relationship Validation Failure|  |
| <a name=\"695\">695</a>|Relationship Not Found|  |
| <a name=\"697\">697</a>|Derived Property Formula No Longer Valid|  |
| <a name=\"698\">698</a>|Story is not available|  |
| <a name=\"703\">703</a>|Corporate Action Does Not Exist|  |
| <a name=\"720\">720</a>|The provided sort and filter combination is not valid|  |
| <a name=\"721\">721</a>|A2B generation failed|  |
| <a name=\"722\">722</a>|Aggregated Return Calculation Failure|  |
| <a name=\"723\">723</a>|Custom Entity Definition Identifier Already In Use|  |
| <a name=\"724\">724</a>|Custom Entity Definition Not Found|  |
| <a name=\"725\">725</a>|The Placement requested was not found.|  |
| <a name=\"726\">726</a>|The Execution requested was not found.|  |
| <a name=\"727\">727</a>|The Block requested was not found.|  |
| <a name=\"728\">728</a>|The Participation requested was not found.|  |
| <a name=\"729\">729</a>|The Package requested was not found.|  |
| <a name=\"730\">730</a>|The OrderInstruction requested was not found.|  |
| <a name=\"732\">732</a>|Custom Entity not found.|  |
| <a name=\"733\">733</a>|Custom Entity Identifier already in use.|  |
| <a name=\"735\">735</a>|Calculation Failed.|  |
| <a name=\"736\">736</a>|An expected key on HttpResponse is missing.|  |
| <a name=\"737\">737</a>|A required fee detail is missing.|  |
| <a name=\"738\">738</a>|Zero rows were returned from Luminesce|  |
| <a name=\"739\">739</a>|Provided Weekend Mask was invalid|  |
| <a name=\"742\">742</a>|Custom Entity fields do not match the definition|  |
| <a name=\"746\">746</a>|The provided sequence is not valid.|  |
| <a name=\"751\">751</a>|The type of the Custom Entity is different than the type provided in the definition.|  |
| <a name=\"752\">752</a>|Luminesce process returned an error.|  |
| <a name=\"753\">753</a>|File name or content incompatible with operation.|  |
| <a name=\"755\">755</a>|Schema of response from Drive is not as expected.|  |
| <a name=\"757\">757</a>|Schema of response from Luminesce is not as expected.|  |
| <a name=\"758\">758</a>|Luminesce timed out.|  |


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.11.3916
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonExperimentalClientCodegen
For more information, please visit [https://www.finbourne.com](https://www.finbourne.com)

## Requirements.

Python &gt;&#x3D;3.9
v3.9 is needed so one can combine classmethod and property decorators to define
object schema properties as classes

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import luisd
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import luisd
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import luisd
from pprint import pprint
from luisd.apis import aggregation_api
from luisd.model.configuration_recipe import ConfigurationRecipe
from luisd.model.create_recipe_request import CreateRecipeRequest
from luisd.model.inline_valuation_request import InlineValuationRequest
from luisd.model.list_aggregation_response import ListAggregationResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_aggregation_query import ResourceListOfAggregationQuery
from luisd.model.valuation_request import ValuationRequest
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aggregation_api.AggregationApi(api_client)
    scope = "z" # str, none_type | The scope of the portfolio
code = "z" # str, none_type | The code of the portfolio
create_recipe_request = CreateRecipeRequest(
        recipe_creation_market_data_scopes=[
            "recipe_creation_market_data_scopes_example"
        ],
        recipe_id=ResourceId(
            scope="scope_example",
            code="code_example",
        ),
        inline_recipe=ConfigurationRecipe(
            scope="z",
            code="z",
            market=MarketContext(
                market_rules=[
                    MarketDataKeyRule(
                        key="key_example",
                        supplier="supplier_example",
                        data_scope="z",
                        quote_type="Price",
                        field="field_example",
                        quote_interval="quote_interval_example",
                        as_at="1970-01-01T00:00:00.00Z",
                        price_source="price_source_example",
                        mask="mask_example",
                    )
                ],
                suppliers=dict(
                    commodity="commodity_example",
                    credit="credit_example",
                    equity="equity_example",
                    fx="fx_example",
                    rates="rates_example",
                ),
                options=MarketOptions(
                    default_supplier="default_supplier_example",
                    default_instrument_code_type="default_instrument_code_type_example",
                    default_scope="z",
                    attempt_to_infer_missing_fx=True,
                    calendar_scope="z",
                    convention_scope="z",
                ),
            ),
            pricing=PricingContext(
                model_rules=[
                    VendorModelRule(
                        supplier="Lusid",
                        model_name="model_name_example",
                        instrument_type="instrument_type_example",
                        parameters="parameters_example",
                        model_options=ModelOptions(),
                        instrument_id="instrument_id_example",
                    )
                ],
                model_choice=dict(
                    "key": ModelSelection(
                        library="Lusid",
                        model="SimpleStatic",
                    ),
                ),
                options=PricingOptions(
                    model_selection=ModelSelection(),
                    use_instrument_type_to_determine_pricer=True,
                    allow_any_instruments_with_sec_uid_to_price_off_lookup=True,
                    allow_partially_successful_evaluation=True,
                    produce_separate_result_for_linear_otc_legs=True,
                    enable_use_of_cached_unit_results=True,
                    window_valuation_on_instrument_start_end=True,
                    remove_contingent_cashflows_in_payment_diary=True,
                    use_child_sub_holding_keys_for_portfolio_expansion=True,
                    validate_domestic_and_quote_currencies_are_consistent=True,
                ),
                result_data_rules=[
                    ResultDataKeyRule(
                        resource_key="resource_key_example",
                        supplier="supplier_example",
                        data_scope="z",
                        document_code="document_code_example",
                        quote_interval="quote_interval_example",
                        as_at="1970-01-01T00:00:00.00Z",
                    )
                ],
            ),
            aggregation=AggregationContext(
                options=AggregationOptions(
                    use_ansi_like_syntax=True,
                    allow_partial_entitlement_success=True,
                ),
            ),
            inherited_recipes=[
                ResourceId()
            ],
            description="Aa6w77ikCX*cKCmv|`K/V",
            holding=HoldingContext(
                tax_lot_level_holdings=True,
            ),
        ),
        as_at="1970-01-01T00:00:00.00Z",
        effective_at="effective_at_example",
    ) # CreateRecipeRequest | The request specifying the parameters to generating the recipe (optional)

    try:
        # [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
        api_response = api_instance.generate_configuration_recipe(scopecodecreate_recipe_request=create_recipe_request)
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling AggregationApi->generate_configuration_recipe: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://www.lusid.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AggregationApi* | [**generate_configuration_recipe**](docs/apis/tags/AggregationApi.md#generate_configuration_recipe) | **post** /api/aggregation/{scope}/{code}/$generateconfigurationrecipe | [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
*AggregationApi* | [**get_queryable_keys**](docs/apis/tags/AggregationApi.md#get_queryable_keys) | **get** /api/results/queryable/keys | [EXPERIMENTAL] GetQueryableKeys: Query the set of supported \&quot;addresses\&quot; that can be queried from the aggregation endpoint.
*AggregationApi* | [**get_valuation**](docs/apis/tags/AggregationApi.md#get_valuation) | **post** /api/aggregation/$valuation | [BETA] GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
*AggregationApi* | [**get_valuation_of_weighted_instruments**](docs/apis/tags/AggregationApi.md#get_valuation_of_weighted_instruments) | **post** /api/aggregation/$valuationinlined | [BETA] GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio
*AllocationsApi* | [**delete_allocation**](docs/apis/tags/AllocationsApi.md#delete_allocation) | **delete** /api/allocations/{scope}/{code} | [EARLY ACCESS] DeleteAllocation: Delete allocation
*AllocationsApi* | [**get_allocation**](docs/apis/tags/AllocationsApi.md#get_allocation) | **get** /api/allocations/{scope}/{code} | [EARLY ACCESS] GetAllocation: Get Allocation
*AllocationsApi* | [**list_allocations**](docs/apis/tags/AllocationsApi.md#list_allocations) | **get** /api/allocations | [EARLY ACCESS] ListAllocations: List Allocations
*AllocationsApi* | [**upsert_allocations**](docs/apis/tags/AllocationsApi.md#upsert_allocations) | **post** /api/allocations | [EARLY ACCESS] UpsertAllocations: Upsert Allocations
*ApplicationMetadataApi* | [**get_excel_addin**](docs/apis/tags/ApplicationMetadataApi.md#get_excel_addin) | **get** /api/metadata/downloads/exceladdin | [EARLY ACCESS] GetExcelAddin: Download Excel Addin
*ApplicationMetadataApi* | [**get_lusid_versions**](docs/apis/tags/ApplicationMetadataApi.md#get_lusid_versions) | **get** /api/metadata/versions | [EARLY ACCESS] GetLusidVersions: Get LUSID versions
*ApplicationMetadataApi* | [**list_access_controlled_resources**](docs/apis/tags/ApplicationMetadataApi.md#list_access_controlled_resources) | **get** /api/metadata/access/resources | [EARLY ACCESS] ListAccessControlledResources: Get resources available for access control
*BlocksApi* | [**delete_block**](docs/apis/tags/BlocksApi.md#delete_block) | **delete** /api/blocks/{scope}/{code} | [EXPERIMENTAL] DeleteBlock: Delete block
*BlocksApi* | [**get_block**](docs/apis/tags/BlocksApi.md#get_block) | **get** /api/blocks/{scope}/{code} | [EXPERIMENTAL] GetBlock: Get Block
*BlocksApi* | [**list_blocks**](docs/apis/tags/BlocksApi.md#list_blocks) | **get** /api/blocks | [EXPERIMENTAL] ListBlocks: List Blocks
*BlocksApi* | [**upsert_blocks**](docs/apis/tags/BlocksApi.md#upsert_blocks) | **post** /api/blocks | [EXPERIMENTAL] UpsertBlocks: Upsert Block
*CalendarsApi* | [**add_business_days_to_date**](docs/apis/tags/CalendarsApi.md#add_business_days_to_date) | **post** /api/calendars/businessday/{scope}/add | [EXPERIMENTAL] AddBusinessDaysToDate: Adds the requested number of Business Days to the provided date.
*CalendarsApi* | [**add_date_to_calendar**](docs/apis/tags/CalendarsApi.md#add_date_to_calendar) | **put** /api/calendars/generic/{scope}/{code}/dates | [BETA] AddDateToCalendar: Add a date to a calendar
*CalendarsApi* | [**create_calendar**](docs/apis/tags/CalendarsApi.md#create_calendar) | **post** /api/calendars/generic | [BETA] CreateCalendar: Create a calendar in its generic form
*CalendarsApi* | [**delete_calendar**](docs/apis/tags/CalendarsApi.md#delete_calendar) | **delete** /api/calendars/generic/{scope}/{code} | [BETA] DeleteCalendar: Delete a calendar
*CalendarsApi* | [**delete_date_from_calendar**](docs/apis/tags/CalendarsApi.md#delete_date_from_calendar) | **delete** /api/calendars/generic/{scope}/{code}/dates/{dateId} | [BETA] DeleteDateFromCalendar: Remove a date from a calendar
*CalendarsApi* | [**generate_schedule**](docs/apis/tags/CalendarsApi.md#generate_schedule) | **post** /api/calendars/schedule/{scope} | [EXPERIMENTAL] GenerateSchedule: Generate an ordered schedule of dates.
*CalendarsApi* | [**get_calendar**](docs/apis/tags/CalendarsApi.md#get_calendar) | **get** /api/calendars/generic/{scope}/{code} | [BETA] GetCalendar: Get a calendar in its generic form
*CalendarsApi* | [**get_dates**](docs/apis/tags/CalendarsApi.md#get_dates) | **get** /api/calendars/generic/{scope}/{code}/dates | [BETA] GetDates: Get dates for a specific calendar
*CalendarsApi* | [**is_business_date_time**](docs/apis/tags/CalendarsApi.md#is_business_date_time) | **get** /api/calendars/businessday/{scope}/{code} | [BETA] IsBusinessDateTime: Check whether a DateTime is a \&quot;Business DateTime\&quot;
*CalendarsApi* | [**list_calendars**](docs/apis/tags/CalendarsApi.md#list_calendars) | **get** /api/calendars/generic | [BETA] ListCalendars: List Calendars
*CalendarsApi* | [**list_calendars_in_scope**](docs/apis/tags/CalendarsApi.md#list_calendars_in_scope) | **get** /api/calendars/generic/{scope} | [BETA] ListCalendarsInScope: List all calenders in a specified scope
*CalendarsApi* | [**update_calendar**](docs/apis/tags/CalendarsApi.md#update_calendar) | **post** /api/calendars/generic/{scope}/{code} | [BETA] UpdateCalendar: Update a calendar
*ComplexMarketDataApi* | [**delete_complex_market_data**](docs/apis/tags/ComplexMarketDataApi.md#delete_complex_market_data) | **post** /api/complexmarketdata/{scope}/$delete | [EARLY ACCESS] DeleteComplexMarketData: Delete one or more items of complex market data, assuming they are present.
*ComplexMarketDataApi* | [**get_complex_market_data**](docs/apis/tags/ComplexMarketDataApi.md#get_complex_market_data) | **post** /api/complexmarketdata/{scope}/$get | [EARLY ACCESS] GetComplexMarketData: Get complex market data
*ComplexMarketDataApi* | [**list_complex_market_data**](docs/apis/tags/ComplexMarketDataApi.md#list_complex_market_data) | **get** /api/complexmarketdata | [EXPERIMENTAL] ListComplexMarketData: List the set of ComplexMarketData
*ComplexMarketDataApi* | [**upsert_complex_market_data**](docs/apis/tags/ComplexMarketDataApi.md#upsert_complex_market_data) | **post** /api/complexmarketdata/{scope} | [EARLY ACCESS] UpsertComplexMarketData: Upsert a set of complex market data items. This creates or updates the data in Lusid.
*ComplianceApi* | [**get_compliance_run**](docs/apis/tags/ComplianceApi.md#get_compliance_run) | **get** /api/compliance/{runId} | [EXPERIMENTAL] GetComplianceRun: Get the details of a single compliance run.
*ComplianceApi* | [**list_compliance_runs**](docs/apis/tags/ComplianceApi.md#list_compliance_runs) | **get** /api/compliance | [EXPERIMENTAL] ListComplianceRuns: List historical compliance runs.
*ComplianceApi* | [**run_compliance_check**](docs/apis/tags/ComplianceApi.md#run_compliance_check) | **post** /api/compliance/run | [EXPERIMENTAL] RunComplianceCheck: Kick off the compliance check process
*ConfigurationRecipeApi* | [**delete_configuration_recipe**](docs/apis/tags/ConfigurationRecipeApi.md#delete_configuration_recipe) | **delete** /api/recipes/{scope}/{code} | [EXPERIMENTAL] DeleteConfigurationRecipe: Delete a Configuration Recipe, assuming that it is present.
*ConfigurationRecipeApi* | [**get_configuration_recipe**](docs/apis/tags/ConfigurationRecipeApi.md#get_configuration_recipe) | **get** /api/recipes/{scope}/{code} | [EXPERIMENTAL] GetConfigurationRecipe: Get Configuration Recipe
*ConfigurationRecipeApi* | [**list_configuration_recipes**](docs/apis/tags/ConfigurationRecipeApi.md#list_configuration_recipes) | **get** /api/recipes | [EXPERIMENTAL] ListConfigurationRecipes: List the set of Configuration Recipes
*ConfigurationRecipeApi* | [**upsert_configuration_recipe**](docs/apis/tags/ConfigurationRecipeApi.md#upsert_configuration_recipe) | **post** /api/recipes | [EXPERIMENTAL] UpsertConfigurationRecipe: Upsert a Configuration Recipe. This creates or updates the data in Lusid.
*ConventionsApi* | [**delete_cds_flow_conventions**](docs/apis/tags/ConventionsApi.md#delete_cds_flow_conventions) | **delete** /api/conventions/credit/conventions/{scope}/{code} | [BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.
*ConventionsApi* | [**delete_flow_conventions**](docs/apis/tags/ConventionsApi.md#delete_flow_conventions) | **delete** /api/conventions/rates/flowconventions/{scope}/{code} | [BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.
*ConventionsApi* | [**delete_index_convention**](docs/apis/tags/ConventionsApi.md#delete_index_convention) | **delete** /api/conventions/rates/indexconventions/{scope}/{code} | [BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.
*ConventionsApi* | [**get_cds_flow_conventions**](docs/apis/tags/ConventionsApi.md#get_cds_flow_conventions) | **get** /api/conventions/credit/conventions/{scope}/{code} | [BETA] GetCdsFlowConventions: Get CDS Flow Conventions
*ConventionsApi* | [**get_flow_conventions**](docs/apis/tags/ConventionsApi.md#get_flow_conventions) | **get** /api/conventions/rates/flowconventions/{scope}/{code} | [BETA] GetFlowConventions: Get Flow Conventions
*ConventionsApi* | [**get_index_convention**](docs/apis/tags/ConventionsApi.md#get_index_convention) | **get** /api/conventions/rates/indexconventions/{scope}/{code} | [BETA] GetIndexConvention: Get Index Convention
*ConventionsApi* | [**list_cds_flow_conventions**](docs/apis/tags/ConventionsApi.md#list_cds_flow_conventions) | **get** /api/conventions/credit/conventions | [BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions
*ConventionsApi* | [**list_flow_conventions**](docs/apis/tags/ConventionsApi.md#list_flow_conventions) | **get** /api/conventions/rates/flowconventions | [BETA] ListFlowConventions: List the set of Flow Conventions
*ConventionsApi* | [**list_index_convention**](docs/apis/tags/ConventionsApi.md#list_index_convention) | **get** /api/conventions/rates/indexconventions | [BETA] ListIndexConvention: List the set of Index Conventions
*ConventionsApi* | [**upsert_cds_flow_conventions**](docs/apis/tags/ConventionsApi.md#upsert_cds_flow_conventions) | **post** /api/conventions/credit/conventions | [BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.
*ConventionsApi* | [**upsert_flow_conventions**](docs/apis/tags/ConventionsApi.md#upsert_flow_conventions) | **post** /api/conventions/rates/flowconventions | [BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.
*ConventionsApi* | [**upsert_index_convention**](docs/apis/tags/ConventionsApi.md#upsert_index_convention) | **post** /api/conventions/rates/indexconventions | [BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.
*CorporateActionSourcesApi* | [**batch_upsert_corporate_actions**](docs/apis/tags/CorporateActionSourcesApi.md#batch_upsert_corporate_actions) | **post** /api/corporateactionsources/{scope}/{code}/corporateactions | [BETA] BatchUpsertCorporateActions: Upsert corporate actions
*CorporateActionSourcesApi* | [**create_corporate_action_source**](docs/apis/tags/CorporateActionSourcesApi.md#create_corporate_action_source) | **post** /api/corporateactionsources | [BETA] CreateCorporateActionSource: Create corporate action source
*CorporateActionSourcesApi* | [**delete_corporate_action_source**](docs/apis/tags/CorporateActionSourcesApi.md#delete_corporate_action_source) | **delete** /api/corporateactionsources/{scope}/{code} | [BETA] DeleteCorporateActionSource: Delete a corporate action source
*CorporateActionSourcesApi* | [**delete_corporate_actions**](docs/apis/tags/CorporateActionSourcesApi.md#delete_corporate_actions) | **delete** /api/corporateactionsources/{scope}/{code}/corporateactions | [EXPERIMENTAL] DeleteCorporateActions: Delete corporate actions
*CorporateActionSourcesApi* | [**get_corporate_actions**](docs/apis/tags/CorporateActionSourcesApi.md#get_corporate_actions) | **get** /api/corporateactionsources/{scope}/{code}/corporateactions | [BETA] GetCorporateActions: Get corporate actions
*CorporateActionSourcesApi* | [**list_corporate_action_sources**](docs/apis/tags/CorporateActionSourcesApi.md#list_corporate_action_sources) | **get** /api/corporateactionsources | [BETA] ListCorporateActionSources: List corporate action sources
*CounterpartiesApi* | [**delete_counterparty_agreement**](docs/apis/tags/CounterpartiesApi.md#delete_counterparty_agreement) | **delete** /api/counterparties/counterpartyagreements/{scope}/{code} | [EXPERIMENTAL] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code
*CounterpartiesApi* | [**delete_credit_support_annex**](docs/apis/tags/CounterpartiesApi.md#delete_credit_support_annex) | **delete** /api/counterparties/creditsupportannexes/{scope}/{code} | [EXPERIMENTAL] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code
*CounterpartiesApi* | [**get_counterparty_agreement**](docs/apis/tags/CounterpartiesApi.md#get_counterparty_agreement) | **get** /api/counterparties/counterpartyagreements/{scope}/{code} | [EXPERIMENTAL] GetCounterpartyAgreement: Get Counterparty Agreement
*CounterpartiesApi* | [**get_credit_support_annex**](docs/apis/tags/CounterpartiesApi.md#get_credit_support_annex) | **get** /api/counterparties/creditsupportannexes/{scope}/{code} | [EXPERIMENTAL] GetCreditSupportAnnex: Get Credit Support Annex
*CounterpartiesApi* | [**list_counterparty_agreements**](docs/apis/tags/CounterpartiesApi.md#list_counterparty_agreements) | **get** /api/counterparties/counterpartyagreements | [EXPERIMENTAL] ListCounterpartyAgreements: List the set of Counterparty Agreements
*CounterpartiesApi* | [**list_credit_support_annexes**](docs/apis/tags/CounterpartiesApi.md#list_credit_support_annexes) | **get** /api/counterparties/creditsupportannexes | [EXPERIMENTAL] ListCreditSupportAnnexes: List the set of Credit Support Annexes
*CounterpartiesApi* | [**upsert_counterparty_agreement**](docs/apis/tags/CounterpartiesApi.md#upsert_counterparty_agreement) | **post** /api/counterparties/counterpartyagreements | [EXPERIMENTAL] UpsertCounterpartyAgreement: Upsert Counterparty Agreement
*CounterpartiesApi* | [**upsert_credit_support_annex**](docs/apis/tags/CounterpartiesApi.md#upsert_credit_support_annex) | **post** /api/counterparties/creditsupportannexes | [EXPERIMENTAL] UpsertCreditSupportAnnex: Upsert Credit Support Annex
*CustomEntitiesApi* | [**get_custom_entity**](docs/apis/tags/CustomEntitiesApi.md#get_custom_entity) | **get** /api/customentities/{entityType}/{identifierType}/{identifierValue} | [EXPERIMENTAL] GetCustomEntity: Get CustomEntity
*CustomEntitiesApi* | [**get_custom_entity_relationships**](docs/apis/tags/CustomEntitiesApi.md#get_custom_entity_relationships) | **get** /api/customentities/{entityType}/{identifierType}/{identifierValue}/relationships | [EXPERIMENTAL] GetCustomEntityRelationships: Get Relationships for Custom Entity
*CustomEntitiesApi* | [**list_custom_entities**](docs/apis/tags/CustomEntitiesApi.md#list_custom_entities) | **get** /api/customentities/{entityType} | [EXPERIMENTAL] ListCustomEntities: List Custom Entities
*CustomEntitiesApi* | [**upsert_custom_entity**](docs/apis/tags/CustomEntitiesApi.md#upsert_custom_entity) | **post** /api/customentities/{entityType} | [EXPERIMENTAL] UpsertCustomEntity: Upsert a new CustomEntity
*CustomEntityDefinitionsApi* | [**create_custom_entity_definition**](docs/apis/tags/CustomEntityDefinitionsApi.md#create_custom_entity_definition) | **post** /api/customentities/entitytypes | [EXPERIMENTAL] CreateCustomEntityDefinition: Create a new CustomEntityDefinition
*CustomEntityDefinitionsApi* | [**get_definition**](docs/apis/tags/CustomEntityDefinitionsApi.md#get_definition) | **get** /api/customentities/entitytypes/{entityType} | [EXPERIMENTAL] GetDefinition: Get CustomEntityDefinition
*CutLabelDefinitionsApi* | [**create_cut_label_definition**](docs/apis/tags/CutLabelDefinitionsApi.md#create_cut_label_definition) | **post** /api/systemconfiguration/cutlabels | [EARLY ACCESS] CreateCutLabelDefinition: Create a Cut Label
*CutLabelDefinitionsApi* | [**delete_cut_label_definition**](docs/apis/tags/CutLabelDefinitionsApi.md#delete_cut_label_definition) | **delete** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] DeleteCutLabelDefinition: Delete a Cut Label
*CutLabelDefinitionsApi* | [**get_cut_label_definition**](docs/apis/tags/CutLabelDefinitionsApi.md#get_cut_label_definition) | **get** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] GetCutLabelDefinition: Get a Cut Label
*CutLabelDefinitionsApi* | [**list_cut_label_definitions**](docs/apis/tags/CutLabelDefinitionsApi.md#list_cut_label_definitions) | **get** /api/systemconfiguration/cutlabels | [EARLY ACCESS] ListCutLabelDefinitions: List Existing Cut Labels
*CutLabelDefinitionsApi* | [**update_cut_label_definition**](docs/apis/tags/CutLabelDefinitionsApi.md#update_cut_label_definition) | **put** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] UpdateCutLabelDefinition: Update a Cut Label
*DataTypesApi* | [**create_data_type**](docs/apis/tags/DataTypesApi.md#create_data_type) | **post** /api/datatypes | [BETA] CreateDataType: Create data type definition
*DataTypesApi* | [**get_data_type**](docs/apis/tags/DataTypesApi.md#get_data_type) | **get** /api/datatypes/{scope}/{code} | [EARLY ACCESS] GetDataType: Get data type definition
*DataTypesApi* | [**get_units_from_data_type**](docs/apis/tags/DataTypesApi.md#get_units_from_data_type) | **get** /api/datatypes/{scope}/{code}/units | [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
*DataTypesApi* | [**list_data_type_summaries**](docs/apis/tags/DataTypesApi.md#list_data_type_summaries) | **get** /api/datatypes | [EXPERIMENTAL] ListDataTypeSummaries: List all data type summaries, without the reference data
*DataTypesApi* | [**list_data_types**](docs/apis/tags/DataTypesApi.md#list_data_types) | **get** /api/datatypes/{scope} | [EARLY ACCESS] ListDataTypes: List data types
*DataTypesApi* | [**update_data_type**](docs/apis/tags/DataTypesApi.md#update_data_type) | **put** /api/datatypes/{scope}/{code} | [EXPERIMENTAL] UpdateDataType: Update data type definition
*DataTypesApi* | [**update_reference_values**](docs/apis/tags/DataTypesApi.md#update_reference_values) | **put** /api/datatypes/{scope}/{code}/referencedatavalues | [EXPERIMENTAL] UpdateReferenceValues: Update reference data on a data type
*DerivedTransactionPortfoliosApi* | [**create_derived_portfolio**](docs/apis/tags/DerivedTransactionPortfoliosApi.md#create_derived_portfolio) | **post** /api/derivedtransactionportfolios/{scope} | [EARLY ACCESS] CreateDerivedPortfolio: Create derived portfolio
*DerivedTransactionPortfoliosApi* | [**delete_derived_portfolio_details**](docs/apis/tags/DerivedTransactionPortfoliosApi.md#delete_derived_portfolio_details) | **delete** /api/derivedtransactionportfolios/{scope}/{code}/details | [EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details
*EntitiesApi* | [**get_portfolio_changes**](docs/apis/tags/EntitiesApi.md#get_portfolio_changes) | **get** /api/entities/changes/portfolios | [EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.
*ExecutionsApi* | [**delete_execution**](docs/apis/tags/ExecutionsApi.md#delete_execution) | **delete** /api/executions/{scope}/{code} | [EXPERIMENTAL] DeleteExecution: Delete execution
*ExecutionsApi* | [**get_execution**](docs/apis/tags/ExecutionsApi.md#get_execution) | **get** /api/executions/{scope}/{code} | [EXPERIMENTAL] GetExecution: Get Execution
*ExecutionsApi* | [**list_executions**](docs/apis/tags/ExecutionsApi.md#list_executions) | **get** /api/executions | [EXPERIMENTAL] ListExecutions: List Executions
*ExecutionsApi* | [**upsert_executions**](docs/apis/tags/ExecutionsApi.md#upsert_executions) | **post** /api/executions | [EXPERIMENTAL] UpsertExecutions: Upsert Execution
*FeesAndCommissionsApi* | [**get_applicable_fees**](docs/apis/tags/FeesAndCommissionsApi.md#get_applicable_fees) | **get** /api/feesandcommissions | [EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.
*FeesAndCommissionsApi* | [**list_all_fees**](docs/apis/tags/FeesAndCommissionsApi.md#list_all_fees) | **get** /api/feesandcommissions/rules | [EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.
*InstrumentsApi* | [**delete_instrument**](docs/apis/tags/InstrumentsApi.md#delete_instrument) | **delete** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] DeleteInstrument: Delete instrument
*InstrumentsApi* | [**delete_instrument_properties**](docs/apis/tags/InstrumentsApi.md#delete_instrument_properties) | **post** /api/instruments/{identifierType}/{identifier}/properties/$delete | [EXPERIMENTAL] DeleteInstrumentProperties: Delete instrument properties
*InstrumentsApi* | [**get_instrument**](docs/apis/tags/InstrumentsApi.md#get_instrument) | **get** /api/instruments/{identifierType}/{identifier} | GetInstrument: Get instrument
*InstrumentsApi* | [**get_instrument_identifier_types**](docs/apis/tags/InstrumentsApi.md#get_instrument_identifier_types) | **get** /api/instruments/identifierTypes | [EARLY ACCESS] GetInstrumentIdentifierTypes: Get instrument identifier types
*InstrumentsApi* | [**get_instrument_properties**](docs/apis/tags/InstrumentsApi.md#get_instrument_properties) | **get** /api/instruments/{identifierType}/{identifier}/properties | [EXPERIMENTAL] GetInstrumentProperties: Get instrument properties
*InstrumentsApi* | [**get_instrument_property_time_series**](docs/apis/tags/InstrumentsApi.md#get_instrument_property_time_series) | **get** /api/instruments/{identifierType}/{identifier}/properties/time-series | [EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series
*InstrumentsApi* | [**get_instruments**](docs/apis/tags/InstrumentsApi.md#get_instruments) | **post** /api/instruments/$get | GetInstruments: Get instruments
*InstrumentsApi* | [**list_instrument_properties**](docs/apis/tags/InstrumentsApi.md#list_instrument_properties) | **get** /api/instruments/{identifierType}/{identifier}/properties/list | [EXPERIMENTAL] ListInstrumentProperties: Get instrument properties (with Pagination)
*InstrumentsApi* | [**list_instruments**](docs/apis/tags/InstrumentsApi.md#list_instruments) | **get** /api/instruments | [EARLY ACCESS] ListInstruments: List instruments
*InstrumentsApi* | [**update_instrument_identifier**](docs/apis/tags/InstrumentsApi.md#update_instrument_identifier) | **post** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] UpdateInstrumentIdentifier: Update instrument identifier
*InstrumentsApi* | [**upsert_instruments**](docs/apis/tags/InstrumentsApi.md#upsert_instruments) | **post** /api/instruments | UpsertInstruments: Upsert instruments
*InstrumentsApi* | [**upsert_instruments_properties**](docs/apis/tags/InstrumentsApi.md#upsert_instruments_properties) | **post** /api/instruments/$upsertproperties | UpsertInstrumentsProperties: Upsert instruments properties
*LegalEntitiesApi* | [**delete_legal_entity**](docs/apis/tags/LegalEntitiesApi.md#delete_legal_entity) | **delete** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] DeleteLegalEntity: Delete Legal Entity
*LegalEntitiesApi* | [**delete_legal_entity_access_metadata**](docs/apis/tags/LegalEntitiesApi.md#delete_legal_entity_access_metadata) | **delete** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteLegalEntityAccessMetadata: Delete a Legal Entity Access Metadata entry
*LegalEntitiesApi* | [**delete_legal_entity_identifiers**](docs/apis/tags/LegalEntitiesApi.md#delete_legal_entity_identifiers) | **delete** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] DeleteLegalEntityIdentifiers: Delete Legal Entity Identifiers
*LegalEntitiesApi* | [**delete_legal_entity_properties**](docs/apis/tags/LegalEntitiesApi.md#delete_legal_entity_properties) | **delete** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] DeleteLegalEntityProperties: Delete Legal Entity Properties
*LegalEntitiesApi* | [**get_all_legal_entity_access_metadata**](docs/apis/tags/LegalEntitiesApi.md#get_all_legal_entity_access_metadata) | **get** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] GetAllLegalEntityAccessMetadata: Get Access Metadata rules for a Legal Entity
*LegalEntitiesApi* | [**get_legal_entity**](docs/apis/tags/LegalEntitiesApi.md#get_legal_entity) | **get** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] GetLegalEntity: Get Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_access_metadata_by_key**](docs/apis/tags/LegalEntitiesApi.md#get_legal_entity_access_metadata_by_key) | **get** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetLegalEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_property_time_series**](docs/apis/tags/LegalEntitiesApi.md#get_legal_entity_property_time_series) | **get** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | [EXPERIMENTAL] GetLegalEntityPropertyTimeSeries: Get Legal Entity Property Time Series
*LegalEntitiesApi* | [**get_legal_entity_relations**](docs/apis/tags/LegalEntitiesApi.md#get_legal_entity_relations) | **get** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/relations | [EXPERIMENTAL] GetLegalEntityRelations: Get Relations for Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_relationships**](docs/apis/tags/LegalEntitiesApi.md#get_legal_entity_relationships) | **get** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/relationships | [EXPERIMENTAL] GetLegalEntityRelationships: Get Relationships for Legal Entity
*LegalEntitiesApi* | [**list_legal_entities**](docs/apis/tags/LegalEntitiesApi.md#list_legal_entities) | **get** /api/legalentities/{idTypeScope}/{idTypeCode} | [EARLY ACCESS] ListLegalEntities: List Legal Entities
*LegalEntitiesApi* | [**set_legal_entity_identifiers**](docs/apis/tags/LegalEntitiesApi.md#set_legal_entity_identifiers) | **post** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] SetLegalEntityIdentifiers: Set Legal Entity Identifiers
*LegalEntitiesApi* | [**upsert_legal_entity**](docs/apis/tags/LegalEntitiesApi.md#upsert_legal_entity) | **post** /api/legalentities | [EARLY ACCESS] UpsertLegalEntity: Upsert Legal Entity
*LegalEntitiesApi* | [**upsert_legal_entity_access_metadata**](docs/apis/tags/LegalEntitiesApi.md#upsert_legal_entity_access_metadata) | **put** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertLegalEntityAccessMetadata: Upsert a Legal Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*OrderGraphApi* | [**list_order_graph_blocks**](docs/apis/tags/OrderGraphApi.md#list_order_graph_blocks) | **get** /api/ordergraph/blocks | [EXPERIMENTAL] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
*OrderGraphApi* | [**list_order_graph_placements**](docs/apis/tags/OrderGraphApi.md#list_order_graph_placements) | **get** /api/ordergraph/placements | [EXPERIMENTAL] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.
*OrderInstructionsApi* | [**delete_order_instruction**](docs/apis/tags/OrderInstructionsApi.md#delete_order_instruction) | **delete** /api/orderinstructions/{scope}/{code} | [EXPERIMENTAL] DeleteOrderInstruction: Delete orderInstruction
*OrderInstructionsApi* | [**get_order_instruction**](docs/apis/tags/OrderInstructionsApi.md#get_order_instruction) | **get** /api/orderinstructions/{scope}/{code} | [EXPERIMENTAL] GetOrderInstruction: Get OrderInstruction
*OrderInstructionsApi* | [**list_order_instructions**](docs/apis/tags/OrderInstructionsApi.md#list_order_instructions) | **get** /api/orderinstructions | [EXPERIMENTAL] ListOrderInstructions: List OrderInstructions
*OrderInstructionsApi* | [**upsert_order_instructions**](docs/apis/tags/OrderInstructionsApi.md#upsert_order_instructions) | **post** /api/orderinstructions | [EXPERIMENTAL] UpsertOrderInstructions: Upsert OrderInstruction
*OrdersApi* | [**delete_order**](docs/apis/tags/OrdersApi.md#delete_order) | **delete** /api/orders/{scope}/{code} | [EARLY ACCESS] DeleteOrder: Delete order
*OrdersApi* | [**get_order**](docs/apis/tags/OrdersApi.md#get_order) | **get** /api/orders/{scope}/{code} | [EARLY ACCESS] GetOrder: Get Order
*OrdersApi* | [**list_orders**](docs/apis/tags/OrdersApi.md#list_orders) | **get** /api/orders | [EARLY ACCESS] ListOrders: List Orders
*OrdersApi* | [**upsert_orders**](docs/apis/tags/OrdersApi.md#upsert_orders) | **post** /api/orders | [EARLY ACCESS] UpsertOrders: Upsert Order
*PackagesApi* | [**delete_package**](docs/apis/tags/PackagesApi.md#delete_package) | **delete** /api/packages/{scope}/{code} | [EXPERIMENTAL] DeletePackage: Delete package
*PackagesApi* | [**get_package**](docs/apis/tags/PackagesApi.md#get_package) | **get** /api/packages/{scope}/{code} | [EXPERIMENTAL] GetPackage: Get Package
*PackagesApi* | [**list_packages**](docs/apis/tags/PackagesApi.md#list_packages) | **get** /api/packages | [EXPERIMENTAL] ListPackages: List Packages
*PackagesApi* | [**upsert_packages**](docs/apis/tags/PackagesApi.md#upsert_packages) | **post** /api/packages | [EXPERIMENTAL] UpsertPackages: Upsert Package
*ParticipationsApi* | [**delete_participation**](docs/apis/tags/ParticipationsApi.md#delete_participation) | **delete** /api/participations/{scope}/{code} | [EXPERIMENTAL] DeleteParticipation: Delete participation
*ParticipationsApi* | [**get_participation**](docs/apis/tags/ParticipationsApi.md#get_participation) | **get** /api/participations/{scope}/{code} | [EXPERIMENTAL] GetParticipation: Get Participation
*ParticipationsApi* | [**list_participations**](docs/apis/tags/ParticipationsApi.md#list_participations) | **get** /api/participations | [EXPERIMENTAL] ListParticipations: List Participations
*ParticipationsApi* | [**upsert_participations**](docs/apis/tags/ParticipationsApi.md#upsert_participations) | **post** /api/participations | [EXPERIMENTAL] UpsertParticipations: Upsert Participation
*PersonsApi* | [**delete_person**](docs/apis/tags/PersonsApi.md#delete_person) | **delete** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] DeletePerson: Delete person
*PersonsApi* | [**delete_person_access_metadata**](docs/apis/tags/PersonsApi.md#delete_person_access_metadata) | **delete** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry
*PersonsApi* | [**delete_person_identifiers**](docs/apis/tags/PersonsApi.md#delete_person_identifiers) | **delete** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] DeletePersonIdentifiers: Delete Person Identifiers
*PersonsApi* | [**delete_person_properties**](docs/apis/tags/PersonsApi.md#delete_person_properties) | **delete** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] DeletePersonProperties: Delete Person Properties
*PersonsApi* | [**get_all_person_access_metadata**](docs/apis/tags/PersonsApi.md#get_all_person_access_metadata) | **get** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person
*PersonsApi* | [**get_person**](docs/apis/tags/PersonsApi.md#get_person) | **get** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] GetPerson: Get Person
*PersonsApi* | [**get_person_access_metadata_by_key**](docs/apis/tags/PersonsApi.md#get_person_access_metadata_by_key) | **get** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person
*PersonsApi* | [**get_person_property_time_series**](docs/apis/tags/PersonsApi.md#get_person_property_time_series) | **get** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | [EXPERIMENTAL] GetPersonPropertyTimeSeries: Get Person Property Time Series
*PersonsApi* | [**get_person_relations**](docs/apis/tags/PersonsApi.md#get_person_relations) | **get** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relations | [EXPERIMENTAL] GetPersonRelations: Get Relations for Person
*PersonsApi* | [**get_person_relationships**](docs/apis/tags/PersonsApi.md#get_person_relationships) | **get** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relationships | [EXPERIMENTAL] GetPersonRelationships: Get Relationships for Person
*PersonsApi* | [**list_persons**](docs/apis/tags/PersonsApi.md#list_persons) | **get** /api/persons/{idTypeScope}/{idTypeCode} | [EXPERIMENTAL] ListPersons: List Persons
*PersonsApi* | [**set_person_identifiers**](docs/apis/tags/PersonsApi.md#set_person_identifiers) | **post** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] SetPersonIdentifiers: Set Person Identifiers
*PersonsApi* | [**set_person_properties**](docs/apis/tags/PersonsApi.md#set_person_properties) | **post** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] SetPersonProperties: Set Person Properties
*PersonsApi* | [**upsert_person**](docs/apis/tags/PersonsApi.md#upsert_person) | **post** /api/persons | [EXPERIMENTAL] UpsertPerson: Upsert Person
*PersonsApi* | [**upsert_person_access_metadata**](docs/apis/tags/PersonsApi.md#upsert_person_access_metadata) | **put** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*PlacementsApi* | [**delete_placement**](docs/apis/tags/PlacementsApi.md#delete_placement) | **delete** /api/placements/{scope}/{code} | [EXPERIMENTAL] DeletePlacement: Delete placement
*PlacementsApi* | [**get_placement**](docs/apis/tags/PlacementsApi.md#get_placement) | **get** /api/placements/{scope}/{code} | [EXPERIMENTAL] GetPlacement: Get Placement
*PlacementsApi* | [**list_placements**](docs/apis/tags/PlacementsApi.md#list_placements) | **get** /api/placements | [EXPERIMENTAL] ListPlacements: List Placements
*PlacementsApi* | [**upsert_placements**](docs/apis/tags/PlacementsApi.md#upsert_placements) | **post** /api/placements | [EXPERIMENTAL] UpsertPlacements: Upsert Placement
*PortfolioGroupsApi* | [**add_portfolio_to_group**](docs/apis/tags/PortfolioGroupsApi.md#add_portfolio_to_group) | **post** /api/portfoliogroups/{scope}/{code}/portfolios | [EARLY ACCESS] AddPortfolioToGroup: Add portfolio to group
*PortfolioGroupsApi* | [**add_sub_group_to_group**](docs/apis/tags/PortfolioGroupsApi.md#add_sub_group_to_group) | **post** /api/portfoliogroups/{scope}/{code}/subgroups | [EARLY ACCESS] AddSubGroupToGroup: Add sub group to group
*PortfolioGroupsApi* | [**build_transactions_for_portfolio_group**](docs/apis/tags/PortfolioGroupsApi.md#build_transactions_for_portfolio_group) | **post** /api/portfoliogroups/{scope}/{code}/transactions/$build | [EARLY ACCESS] BuildTransactionsForPortfolioGroup: Build transactions for transaction portfolios in a portfolio group
*PortfolioGroupsApi* | [**create_portfolio_group**](docs/apis/tags/PortfolioGroupsApi.md#create_portfolio_group) | **post** /api/portfoliogroups/{scope} | [EARLY ACCESS] CreatePortfolioGroup: Create portfolio group
*PortfolioGroupsApi* | [**delete_group_properties**](docs/apis/tags/PortfolioGroupsApi.md#delete_group_properties) | **post** /api/portfoliogroups/{scope}/{code}/properties/$delete | [EARLY ACCESS] DeleteGroupProperties: Delete group properties
*PortfolioGroupsApi* | [**delete_key_from_portfolio_group_access_metadata**](docs/apis/tags/PortfolioGroupsApi.md#delete_key_from_portfolio_group_access_metadata) | **delete** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteKeyFromPortfolioGroupAccessMetadata: Delete a Portfolio Group Access Metadata entry
*PortfolioGroupsApi* | [**delete_portfolio_from_group**](docs/apis/tags/PortfolioGroupsApi.md#delete_portfolio_from_group) | **delete** /api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode} | [EARLY ACCESS] DeletePortfolioFromGroup: Delete portfolio from group
*PortfolioGroupsApi* | [**delete_portfolio_group**](docs/apis/tags/PortfolioGroupsApi.md#delete_portfolio_group) | **delete** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] DeletePortfolioGroup: Delete portfolio group
*PortfolioGroupsApi* | [**delete_sub_group_from_group**](docs/apis/tags/PortfolioGroupsApi.md#delete_sub_group_from_group) | **delete** /api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode} | [EARLY ACCESS] DeleteSubGroupFromGroup: Delete sub group from group
*PortfolioGroupsApi* | [**get_a2_b_data_for_portfolio_group**](docs/apis/tags/PortfolioGroupsApi.md#get_a2_b_data_for_portfolio_group) | **get** /api/portfoliogroups/{scope}/{code}/a2b | [EXPERIMENTAL] GetA2BDataForPortfolioGroup: Get A2B data for a Portfolio Group
*PortfolioGroupsApi* | [**get_group_properties**](docs/apis/tags/PortfolioGroupsApi.md#get_group_properties) | **get** /api/portfoliogroups/{scope}/{code}/properties | [EARLY ACCESS] GetGroupProperties: Get group properties
*PortfolioGroupsApi* | [**get_holdings_for_portfolio_group**](docs/apis/tags/PortfolioGroupsApi.md#get_holdings_for_portfolio_group) | **get** /api/portfoliogroups/{scope}/{code}/holdings | [EARLY ACCESS] GetHoldingsForPortfolioGroup: Get holdings for transaction portfolios in portfolio group
*PortfolioGroupsApi* | [**get_portfolio_group**](docs/apis/tags/PortfolioGroupsApi.md#get_portfolio_group) | **get** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] GetPortfolioGroup: Get portfolio group
*PortfolioGroupsApi* | [**get_portfolio_group_access_metadata_by_key**](docs/apis/tags/PortfolioGroupsApi.md#get_portfolio_group_access_metadata_by_key) | **get** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfolioGroupAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_commands**](docs/apis/tags/PortfolioGroupsApi.md#get_portfolio_group_commands) | **get** /api/portfoliogroups/{scope}/{code}/commands | [EARLY ACCESS] GetPortfolioGroupCommands: Get portfolio group commands
*PortfolioGroupsApi* | [**get_portfolio_group_expansion**](docs/apis/tags/PortfolioGroupsApi.md#get_portfolio_group_expansion) | **get** /api/portfoliogroups/{scope}/{code}/expansion | [EARLY ACCESS] GetPortfolioGroupExpansion: Get portfolio group expansion
*PortfolioGroupsApi* | [**get_portfolio_group_metadata**](docs/apis/tags/PortfolioGroupsApi.md#get_portfolio_group_metadata) | **get** /api/portfoliogroups/{scope}/{code}/metadata | [EARLY ACCESS] GetPortfolioGroupMetadata: Get Access Metadata rules for Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_property_time_series**](docs/apis/tags/PortfolioGroupsApi.md#get_portfolio_group_property_time_series) | **get** /api/portfoliogroups/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPortfolioGroupPropertyTimeSeries: Get the time series of a portfolio group property
*PortfolioGroupsApi* | [**get_portfolio_group_relations**](docs/apis/tags/PortfolioGroupsApi.md#get_portfolio_group_relations) | **get** /api/portfoliogroups/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioGroupRelations: Get Relations for Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_relationships**](docs/apis/tags/PortfolioGroupsApi.md#get_portfolio_group_relationships) | **get** /api/portfoliogroups/{scope}/{code}/relationships | [EXPERIMENTAL] GetPortfolioGroupRelationships: Get Relationships for Portfolio Group
*PortfolioGroupsApi* | [**get_transactions_for_portfolio_group**](docs/apis/tags/PortfolioGroupsApi.md#get_transactions_for_portfolio_group) | **get** /api/portfoliogroups/{scope}/{code}/transactions | [EARLY ACCESS] GetTransactionsForPortfolioGroup: Get transactions for transaction portfolios in a portfolio group
*PortfolioGroupsApi* | [**list_portfolio_groups**](docs/apis/tags/PortfolioGroupsApi.md#list_portfolio_groups) | **get** /api/portfoliogroups/{scope} | [EARLY ACCESS] ListPortfolioGroups: List portfolio groups
*PortfolioGroupsApi* | [**update_portfolio_group**](docs/apis/tags/PortfolioGroupsApi.md#update_portfolio_group) | **put** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] UpdatePortfolioGroup: Update portfolio group
*PortfolioGroupsApi* | [**upsert_group_properties**](docs/apis/tags/PortfolioGroupsApi.md#upsert_group_properties) | **post** /api/portfoliogroups/{scope}/{code}/properties/$upsert | [EARLY ACCESS] UpsertGroupProperties: Upsert group properties
*PortfolioGroupsApi* | [**upsert_portfolio_group_access_metadata**](docs/apis/tags/PortfolioGroupsApi.md#upsert_portfolio_group_access_metadata) | **put** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPortfolioGroupAccessMetadata: Upsert a Portfolio Group Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*PortfoliosApi* | [**delete_key_from_portfolio_access_metadata**](docs/apis/tags/PortfoliosApi.md#delete_key_from_portfolio_access_metadata) | **delete** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteKeyFromPortfolioAccessMetadata: Delete a Portfolio Access Metadata Rule
*PortfoliosApi* | [**delete_portfolio**](docs/apis/tags/PortfoliosApi.md#delete_portfolio) | **delete** /api/portfolios/{scope}/{code} | DeletePortfolio: Delete portfolio
*PortfoliosApi* | [**delete_portfolio_properties**](docs/apis/tags/PortfoliosApi.md#delete_portfolio_properties) | **delete** /api/portfolios/{scope}/{code}/properties | DeletePortfolioProperties: Delete portfolio properties
*PortfoliosApi* | [**delete_portfolio_returns**](docs/apis/tags/PortfoliosApi.md#delete_portfolio_returns) | **delete** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$delete | [EARLY ACCESS] DeletePortfolioReturns: Delete Returns
*PortfoliosApi* | [**get_portfolio**](docs/apis/tags/PortfoliosApi.md#get_portfolio) | **get** /api/portfolios/{scope}/{code} | GetPortfolio: Get portfolio
*PortfoliosApi* | [**get_portfolio_aggregate_returns**](docs/apis/tags/PortfoliosApi.md#get_portfolio_aggregate_returns) | **get** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/aggregated | [EXPERIMENTAL] GetPortfolioAggregateReturns: Aggregate Returns (This is a deprecated endpoint).
*PortfoliosApi* | [**get_portfolio_aggregated_returns**](docs/apis/tags/PortfoliosApi.md#get_portfolio_aggregated_returns) | **post** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$aggregated | [EARLY ACCESS] GetPortfolioAggregatedReturns: Aggregated Returns
*PortfoliosApi* | [**get_portfolio_commands**](docs/apis/tags/PortfoliosApi.md#get_portfolio_commands) | **get** /api/portfolios/{scope}/{code}/commands | [EARLY ACCESS] GetPortfolioCommands: Get portfolio commands
*PortfoliosApi* | [**get_portfolio_metadata**](docs/apis/tags/PortfoliosApi.md#get_portfolio_metadata) | **get** /api/portfolios/{scope}/{code}/metadata | [EARLY ACCESS] GetPortfolioMetadata: Get access metadata rules for a portfolio
*PortfoliosApi* | [**get_portfolio_properties**](docs/apis/tags/PortfoliosApi.md#get_portfolio_properties) | **get** /api/portfolios/{scope}/{code}/properties | GetPortfolioProperties: Get portfolio properties
*PortfoliosApi* | [**get_portfolio_property_time_series**](docs/apis/tags/PortfoliosApi.md#get_portfolio_property_time_series) | **get** /api/portfolios/{scope}/{code}/properties/time-series | [EXPERIMENTAL] GetPortfolioPropertyTimeSeries: Get portfolio property time series
*PortfoliosApi* | [**get_portfolio_relations**](docs/apis/tags/PortfoliosApi.md#get_portfolio_relations) | **get** /api/portfolios/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioRelations: Get portfolio relations
*PortfoliosApi* | [**get_portfolio_relationships**](docs/apis/tags/PortfoliosApi.md#get_portfolio_relationships) | **get** /api/portfolios/{scope}/{code}/relationships | [EXPERIMENTAL] GetPortfolioRelationships: Get portfolio relationships
*PortfoliosApi* | [**get_portfolio_returns**](docs/apis/tags/PortfoliosApi.md#get_portfolio_returns) | **get** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | [EARLY ACCESS] GetPortfolioReturns: Get Returns
*PortfoliosApi* | [**get_portfolios_access_metadata_by_key**](docs/apis/tags/PortfoliosApi.md#get_portfolios_access_metadata_by_key) | **get** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfoliosAccessMetadataByKey: Get an entry identified by a metadataKey in the access metadata object
*PortfoliosApi* | [**list_portfolio_properties**](docs/apis/tags/PortfoliosApi.md#list_portfolio_properties) | **get** /api/portfolios/{scope}/{code}/properties/list | [EXPERIMENTAL] ListPortfolioProperties: Get portfolio properties
*PortfoliosApi* | [**list_portfolios**](docs/apis/tags/PortfoliosApi.md#list_portfolios) | **get** /api/portfolios | ListPortfolios: List portfolios
*PortfoliosApi* | [**list_portfolios_for_scope**](docs/apis/tags/PortfoliosApi.md#list_portfolios_for_scope) | **get** /api/portfolios/{scope} | ListPortfoliosForScope: List portfolios for scope
*PortfoliosApi* | [**update_portfolio**](docs/apis/tags/PortfoliosApi.md#update_portfolio) | **put** /api/portfolios/{scope}/{code} | UpdatePortfolio: Update portfolio
*PortfoliosApi* | [**upsert_portfolio_access_metadata**](docs/apis/tags/PortfoliosApi.md#upsert_portfolio_access_metadata) | **put** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPortfolioAccessMetadata: Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.
*PortfoliosApi* | [**upsert_portfolio_properties**](docs/apis/tags/PortfoliosApi.md#upsert_portfolio_properties) | **post** /api/portfolios/{scope}/{code}/properties | UpsertPortfolioProperties: Upsert portfolio properties
*PortfoliosApi* | [**upsert_portfolio_returns**](docs/apis/tags/PortfoliosApi.md#upsert_portfolio_returns) | **post** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | [EARLY ACCESS] UpsertPortfolioReturns: Upsert Returns
*PropertyDefinitionsApi* | [**create_derived_property_definition**](docs/apis/tags/PropertyDefinitionsApi.md#create_derived_property_definition) | **post** /api/propertydefinitions/derived | [EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition
*PropertyDefinitionsApi* | [**create_property_definition**](docs/apis/tags/PropertyDefinitionsApi.md#create_property_definition) | **post** /api/propertydefinitions | CreatePropertyDefinition: Create property definition
*PropertyDefinitionsApi* | [**delete_property_definition**](docs/apis/tags/PropertyDefinitionsApi.md#delete_property_definition) | **delete** /api/propertydefinitions/{domain}/{scope}/{code} | DeletePropertyDefinition: Delete property definition
*PropertyDefinitionsApi* | [**get_multiple_property_definitions**](docs/apis/tags/PropertyDefinitionsApi.md#get_multiple_property_definitions) | **get** /api/propertydefinitions | GetMultiplePropertyDefinitions: Get multiple property definitions
*PropertyDefinitionsApi* | [**get_property_definition**](docs/apis/tags/PropertyDefinitionsApi.md#get_property_definition) | **get** /api/propertydefinitions/{domain}/{scope}/{code} | GetPropertyDefinition: Get property definition
*PropertyDefinitionsApi* | [**update_property_definition**](docs/apis/tags/PropertyDefinitionsApi.md#update_property_definition) | **put** /api/propertydefinitions/{domain}/{scope}/{code} | UpdatePropertyDefinition: Update property definition
*QuotesApi* | [**delete_quote_access_metadata_rule**](docs/apis/tags/QuotesApi.md#delete_quote_access_metadata_rule) | **delete** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] DeleteQuoteAccessMetadataRule: Delete a Quote Access Metadata Rule
*QuotesApi* | [**delete_quotes**](docs/apis/tags/QuotesApi.md#delete_quotes) | **post** /api/quotes/{scope}/$delete | [EARLY ACCESS] DeleteQuotes: Delete quotes
*QuotesApi* | [**get_quotes**](docs/apis/tags/QuotesApi.md#get_quotes) | **post** /api/quotes/{scope}/$get | [EARLY ACCESS] GetQuotes: Get quotes
*QuotesApi* | [**get_quotes_access_metadata_rule**](docs/apis/tags/QuotesApi.md#get_quotes_access_metadata_rule) | **get** /api/metadata/quotes/rules | [EXPERIMENTAL] GetQuotesAccessMetadataRule: Get a quote access metadata rule
*QuotesApi* | [**list_quotes**](docs/apis/tags/QuotesApi.md#list_quotes) | **get** /api/quotes/{scope}/$deprecated | [DEPRECATED] ListQuotes: List quotes
*QuotesApi* | [**list_quotes_access_metadata_rules**](docs/apis/tags/QuotesApi.md#list_quotes_access_metadata_rules) | **get** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] ListQuotesAccessMetadataRules: List all quote access metadata rules in a scope
*QuotesApi* | [**list_quotes_for_scope**](docs/apis/tags/QuotesApi.md#list_quotes_for_scope) | **get** /api/quotes/{scope} | [EARLY ACCESS] ListQuotesForScope: List quotes for scope
*QuotesApi* | [**upsert_quote_access_metadata_rule**](docs/apis/tags/QuotesApi.md#upsert_quote_access_metadata_rule) | **post** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] UpsertQuoteAccessMetadataRule: Upsert a Quote Access Metadata Rule. This creates or updates the data in LUSID.
*QuotesApi* | [**upsert_quotes**](docs/apis/tags/QuotesApi.md#upsert_quotes) | **post** /api/quotes/{scope} | [EARLY ACCESS] UpsertQuotes: Upsert quotes
*ReconciliationsApi* | [**reconcile_generic**](docs/apis/tags/ReconciliationsApi.md#reconcile_generic) | **post** /api/portfolios/$reconcileGeneric | [EXPERIMENTAL] ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are &#x27;empty&#x27; or null or zero.
*ReconciliationsApi* | [**reconcile_holdings**](docs/apis/tags/ReconciliationsApi.md#reconcile_holdings) | **post** /api/portfolios/$reconcileholdings | [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
*ReconciliationsApi* | [**reconcile_holdings_preview**](docs/apis/tags/ReconciliationsApi.md#reconcile_holdings_preview) | **post** /api/portfolios/preview/$reconcileholdings | [EXPERIMENTAL] ReconcileHoldingsPreview: Reconcile portfolio holdings with given tolerance
*ReconciliationsApi* | [**reconcile_inline**](docs/apis/tags/ReconciliationsApi.md#reconcile_inline) | **post** /api/portfolios/$reconcileInline | [BETA] ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
*ReconciliationsApi* | [**reconcile_valuation**](docs/apis/tags/ReconciliationsApi.md#reconcile_valuation) | **post** /api/portfolios/$reconcileValuation | [BETA] ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
*ReferencePortfolioApi* | [**create_reference_portfolio**](docs/apis/tags/ReferencePortfolioApi.md#create_reference_portfolio) | **post** /api/referenceportfolios/{scope} | CreateReferencePortfolio: Create reference portfolio
*ReferencePortfolioApi* | [**get_reference_portfolio_constituents**](docs/apis/tags/ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **get** /api/referenceportfolios/{scope}/{code}/constituents | GetReferencePortfolioConstituents: Get reference portfolio constituents
*ReferencePortfolioApi* | [**list_constituents_adjustments**](docs/apis/tags/ReferencePortfolioApi.md#list_constituents_adjustments) | **get** /api/referenceportfolios/{scope}/{code}/constituentsadjustments | ListConstituentsAdjustments: List constituents adjustments
*ReferencePortfolioApi* | [**upsert_reference_portfolio_constituents**](docs/apis/tags/ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **post** /api/referenceportfolios/{scope}/{code}/constituents | UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents
*RelationDefinitionsApi* | [**create_relation_definition**](docs/apis/tags/RelationDefinitionsApi.md#create_relation_definition) | **post** /api/relationdefinitions | [EXPERIMENTAL] CreateRelationDefinition: Create a relation definition
*RelationDefinitionsApi* | [**get_relation_definition**](docs/apis/tags/RelationDefinitionsApi.md#get_relation_definition) | **get** /api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationDefinition: Get relation definition
*RelationsApi* | [**create_relation**](docs/apis/tags/RelationsApi.md#create_relation) | **post** /api/relations/{scope}/{code} | [EXPERIMENTAL] CreateRelation: Create Relation
*RelationsApi* | [**delete_relation**](docs/apis/tags/RelationsApi.md#delete_relation) | **post** /api/relations/{scope}/{code}/$delete | [EXPERIMENTAL] DeleteRelation: Delete a relation
*RelationshipDefinitionsApi* | [**create_relationship_definition**](docs/apis/tags/RelationshipDefinitionsApi.md#create_relationship_definition) | **post** /api/relationshipdefinitions | [EXPERIMENTAL] CreateRelationshipDefinition: Create Relationship Definition
*RelationshipDefinitionsApi* | [**get_relationship_definition**](docs/apis/tags/RelationshipDefinitionsApi.md#get_relationship_definition) | **get** /api/relationshipdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition
*RelationshipDefinitionsApi* | [**list_relationship_definitions**](docs/apis/tags/RelationshipDefinitionsApi.md#list_relationship_definitions) | **get** /api/relationshipdefinitions | [EXPERIMENTAL] ListRelationshipDefinitions: List relationship definitions
*RelationshipDefinitionsApi* | [**update_relationship_definition**](docs/apis/tags/RelationshipDefinitionsApi.md#update_relationship_definition) | **put** /api/relationshipdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateRelationshipDefinition: Update Relationship Definition
*RelationshipsApi* | [**create_relationship**](docs/apis/tags/RelationshipsApi.md#create_relationship) | **post** /api/relationshipdefinitions/{scope}/{code}/relationships | [EXPERIMENTAL] CreateRelationship: Create Relationship
*RelationshipsApi* | [**delete_relationship**](docs/apis/tags/RelationshipsApi.md#delete_relationship) | **post** /api/relationshipdefinitions/{scope}/{code}/relationships/$delete | [EXPERIMENTAL] DeleteRelationship: Delete Relationship
*SchemasApi* | [**get_entity_schema**](docs/apis/tags/SchemasApi.md#get_entity_schema) | **get** /api/schemas/entities/{entity} | [BETA] GetEntitySchema: Get schema
*SchemasApi* | [**get_property_schema**](docs/apis/tags/SchemasApi.md#get_property_schema) | **get** /api/schemas/properties | [BETA] GetPropertySchema: Get property schema
*SchemasApi* | [**get_value_types**](docs/apis/tags/SchemasApi.md#get_value_types) | **get** /api/schemas/types | [BETA] GetValueTypes: Get value types
*SchemasApi* | [**list_entities**](docs/apis/tags/SchemasApi.md#list_entities) | **get** /api/schemas/entities | [BETA] ListEntities: List entities
*ScopesApi* | [**list_scopes**](docs/apis/tags/ScopesApi.md#list_scopes) | **get** /api/scopes | [EARLY ACCESS] ListScopes: List Scopes
*SearchApi* | [**instruments_search**](docs/apis/tags/SearchApi.md#instruments_search) | **post** /api/search/instruments | [EXPERIMENTAL] InstrumentsSearch: Instruments search
*SearchApi* | [**search_portfolio_groups**](docs/apis/tags/SearchApi.md#search_portfolio_groups) | **get** /api/search/portfoliogroups | [EARLY ACCESS] SearchPortfolioGroups: Search Portfolio Groups
*SearchApi* | [**search_portfolios**](docs/apis/tags/SearchApi.md#search_portfolios) | **get** /api/search/portfolios | [EARLY ACCESS] SearchPortfolios: Search Portfolios
*SearchApi* | [**search_properties**](docs/apis/tags/SearchApi.md#search_properties) | **get** /api/search/propertydefinitions | [EARLY ACCESS] SearchProperties: Search Property Definitions
*SequencesApi* | [**create_sequence**](docs/apis/tags/SequencesApi.md#create_sequence) | **post** /api/sequences/{scope} | [EXPERIMENTAL] CreateSequence: Create a new sequence
*SequencesApi* | [**get_sequence**](docs/apis/tags/SequencesApi.md#get_sequence) | **get** /api/sequences/{scope}/{code} | [EXPERIMENTAL] GetSequence: Get a specified sequence
*SequencesApi* | [**list_sequences**](docs/apis/tags/SequencesApi.md#list_sequences) | **get** /api/sequences | [EXPERIMENTAL] ListSequences: List Sequences
*SequencesApi* | [**next**](docs/apis/tags/SequencesApi.md#next) | **get** /api/sequences/{scope}/{code}/next | [EXPERIMENTAL] Next: Get next values from sequence
*StructuredResultDataApi* | [**create_data_map**](docs/apis/tags/StructuredResultDataApi.md#create_data_map) | **post** /api/unitresults/datamap/{scope} | [EXPERIMENTAL] CreateDataMap: Create data map
*StructuredResultDataApi* | [**delete_structured_result_data**](docs/apis/tags/StructuredResultDataApi.md#delete_structured_result_data) | **post** /api/unitresults/{scope}/$delete | [EXPERIMENTAL] DeleteStructuredResultData: Delete structured result data
*StructuredResultDataApi* | [**get_data_map**](docs/apis/tags/StructuredResultDataApi.md#get_data_map) | **post** /api/unitresults/datamap/{scope}/$get | [EXPERIMENTAL] GetDataMap: Get data map
*StructuredResultDataApi* | [**get_structured_result_data**](docs/apis/tags/StructuredResultDataApi.md#get_structured_result_data) | **post** /api/unitresults/{scope}/$get | [EXPERIMENTAL] GetStructuredResultData: Get structured result data
*StructuredResultDataApi* | [**get_virtual_document**](docs/apis/tags/StructuredResultDataApi.md#get_virtual_document) | **post** /api/unitresults/virtualdocument/{scope}/$get | [EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents
*StructuredResultDataApi* | [**upsert_structured_result_data**](docs/apis/tags/StructuredResultDataApi.md#upsert_structured_result_data) | **post** /api/unitresults/{scope} | [BETA] UpsertStructuredResultData: Upsert structured result data
*SystemConfigurationApi* | [**create_configuration_transaction_type**](docs/apis/tags/SystemConfigurationApi.md#create_configuration_transaction_type) | **post** /api/systemconfiguration/transactions/type | [EARLY ACCESS] CreateConfigurationTransactionType: Create transaction type
*SystemConfigurationApi* | [**create_side_definition**](docs/apis/tags/SystemConfigurationApi.md#create_side_definition) | **post** /api/systemconfiguration/transactions/side | [EXPERIMENTAL] CreateSideDefinition: Create side definition
*SystemConfigurationApi* | [**delete_transaction_configuration_source**](docs/apis/tags/SystemConfigurationApi.md#delete_transaction_configuration_source) | **delete** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] DeleteTransactionConfigurationSource: Delete all transaction configurations for a source
*SystemConfigurationApi* | [**get_transaction_configuration_source**](docs/apis/tags/SystemConfigurationApi.md#get_transaction_configuration_source) | **get** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] GetTransactionConfigurationSource: Get all transaction configurations for a source
*SystemConfigurationApi* | [**list_configuration_transaction_types**](docs/apis/tags/SystemConfigurationApi.md#list_configuration_transaction_types) | **get** /api/systemconfiguration/transactions | [EARLY ACCESS] ListConfigurationTransactionTypes: List transaction types
*SystemConfigurationApi* | [**set_configuration_transaction_types**](docs/apis/tags/SystemConfigurationApi.md#set_configuration_transaction_types) | **put** /api/systemconfiguration/transactions | [EXPERIMENTAL] SetConfigurationTransactionTypes: Set transaction types
*SystemConfigurationApi* | [**set_transaction_configuration_source**](docs/apis/tags/SystemConfigurationApi.md#set_transaction_configuration_source) | **put** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] SetTransactionConfigurationSource: Set transaction types for a source
*TransactionPortfoliosApi* | [**adjust_holdings**](docs/apis/tags/TransactionPortfoliosApi.md#adjust_holdings) | **post** /api/transactionportfolios/{scope}/{code}/holdings | AdjustHoldings: Adjust holdings
*TransactionPortfoliosApi* | [**build_transactions**](docs/apis/tags/TransactionPortfoliosApi.md#build_transactions) | **post** /api/transactionportfolios/{scope}/{code}/transactions/$build | BuildTransactions: Build transactions
*TransactionPortfoliosApi* | [**cancel_adjust_holdings**](docs/apis/tags/TransactionPortfoliosApi.md#cancel_adjust_holdings) | **delete** /api/transactionportfolios/{scope}/{code}/holdings | CancelAdjustHoldings: Cancel adjust holdings
*TransactionPortfoliosApi* | [**cancel_transactions**](docs/apis/tags/TransactionPortfoliosApi.md#cancel_transactions) | **delete** /api/transactionportfolios/{scope}/{code}/transactions | CancelTransactions: Cancel transactions
*TransactionPortfoliosApi* | [**create_portfolio**](docs/apis/tags/TransactionPortfoliosApi.md#create_portfolio) | **post** /api/transactionportfolios/{scope} | CreatePortfolio: Create portfolio
*TransactionPortfoliosApi* | [**delete_properties_from_transaction**](docs/apis/tags/TransactionPortfoliosApi.md#delete_properties_from_transaction) | **delete** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | DeletePropertiesFromTransaction: Delete properties from transaction
*TransactionPortfoliosApi* | [**get_a2_b_data**](docs/apis/tags/TransactionPortfoliosApi.md#get_a2_b_data) | **get** /api/transactionportfolios/{scope}/{code}/a2b | [EXPERIMENTAL] GetA2BData: Get A2B data
*TransactionPortfoliosApi* | [**get_a2_b_movements**](docs/apis/tags/TransactionPortfoliosApi.md#get_a2_b_movements) | **get** /api/transactionportfolios/{scope}/{code}/a2bmovements | [EXPERIMENTAL] GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
*TransactionPortfoliosApi* | [**get_bucketed_cash_flows**](docs/apis/tags/TransactionPortfoliosApi.md#get_bucketed_cash_flows) | **post** /api/transactionportfolios/{scope}/{code}/bucketedCashFlows | [EXPERIMENTAL] GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios
*TransactionPortfoliosApi* | [**get_details**](docs/apis/tags/TransactionPortfoliosApi.md#get_details) | **get** /api/transactionportfolios/{scope}/{code}/details | GetDetails: Get details
*TransactionPortfoliosApi* | [**get_holdings**](docs/apis/tags/TransactionPortfoliosApi.md#get_holdings) | **get** /api/transactionportfolios/{scope}/{code}/holdings | GetHoldings: Get holdings
*TransactionPortfoliosApi* | [**get_holdings_adjustment**](docs/apis/tags/TransactionPortfoliosApi.md#get_holdings_adjustment) | **get** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | GetHoldingsAdjustment: Get holdings adjustment
*TransactionPortfoliosApi* | [**get_holdings_with_orders**](docs/apis/tags/TransactionPortfoliosApi.md#get_holdings_with_orders) | **get** /api/transactionportfolios/{scope}/{code}/holdingsWithOrders | [EXPERIMENTAL] GetHoldingsWithOrders: Get holdings with orders
*TransactionPortfoliosApi* | [**get_portfolio_cash_flows**](docs/apis/tags/TransactionPortfoliosApi.md#get_portfolio_cash_flows) | **get** /api/transactionportfolios/{scope}/{code}/cashflows | [BETA] GetPortfolioCashFlows: Get portfolio cash flows
*TransactionPortfoliosApi* | [**get_portfolio_cash_ladder**](docs/apis/tags/TransactionPortfoliosApi.md#get_portfolio_cash_ladder) | **get** /api/transactionportfolios/{scope}/{code}/cashladder | [EXPERIMENTAL] GetPortfolioCashLadder: Get portfolio cash ladder
*TransactionPortfoliosApi* | [**get_portfolio_cash_statement**](docs/apis/tags/TransactionPortfoliosApi.md#get_portfolio_cash_statement) | **get** /api/transactionportfolios/{scope}/{code}/cashstatement | [EARLY ACCESS] GetPortfolioCashStatement: Get portfolio cash statement
*TransactionPortfoliosApi* | [**get_transactions**](docs/apis/tags/TransactionPortfoliosApi.md#get_transactions) | **get** /api/transactionportfolios/{scope}/{code}/transactions | GetTransactions: Get transactions
*TransactionPortfoliosApi* | [**get_upsertable_portfolio_cash_flows**](docs/apis/tags/TransactionPortfoliosApi.md#get_upsertable_portfolio_cash_flows) | **get** /api/transactionportfolios/{scope}/{code}/upsertablecashflows | [BETA] GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.
*TransactionPortfoliosApi* | [**list_holdings_adjustments**](docs/apis/tags/TransactionPortfoliosApi.md#list_holdings_adjustments) | **get** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | ListHoldingsAdjustments: List holdings adjustments
*TransactionPortfoliosApi* | [**patch_portfolio_details**](docs/apis/tags/TransactionPortfoliosApi.md#patch_portfolio_details) | **patch** /api/transactionportfolios/{scope}/{code}/details | [EXPERIMENTAL] PatchPortfolioDetails: Patch portfolio details
*TransactionPortfoliosApi* | [**resolve_instrument**](docs/apis/tags/TransactionPortfoliosApi.md#resolve_instrument) | **post** /api/transactionportfolios/{scope}/{code}/$resolve | [EARLY ACCESS] ResolveInstrument: Resolve instrument
*TransactionPortfoliosApi* | [**set_holdings**](docs/apis/tags/TransactionPortfoliosApi.md#set_holdings) | **put** /api/transactionportfolios/{scope}/{code}/holdings | SetHoldings: Set holdings
*TransactionPortfoliosApi* | [**upsert_portfolio_details**](docs/apis/tags/TransactionPortfoliosApi.md#upsert_portfolio_details) | **post** /api/transactionportfolios/{scope}/{code}/details | UpsertPortfolioDetails: Upsert portfolio details
*TransactionPortfoliosApi* | [**upsert_transaction_properties**](docs/apis/tags/TransactionPortfoliosApi.md#upsert_transaction_properties) | **post** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | UpsertTransactionProperties: Upsert transaction properties
*TransactionPortfoliosApi* | [**upsert_transactions**](docs/apis/tags/TransactionPortfoliosApi.md#upsert_transactions) | **post** /api/transactionportfolios/{scope}/{code}/transactions | UpsertTransactions: Upsert transactions
*TranslationApi* | [**translate_instrument_definitions**](docs/apis/tags/TranslationApi.md#translate_instrument_definitions) | **post** /api/translation/instrumentdefinitions | [EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments

## Documentation For Models

 - [A2BBreakdown](docs/models/A2BBreakdown.md)
 - [A2BCategory](docs/models/A2BCategory.md)
 - [A2BDataRecord](docs/models/A2BDataRecord.md)
 - [A2BMovementRecord](docs/models/A2BMovementRecord.md)
 - [AccessControlledAction](docs/models/AccessControlledAction.md)
 - [AccessControlledResource](docs/models/AccessControlledResource.md)
 - [AccessMetadataValue](docs/models/AccessMetadataValue.md)
 - [AccountingMethod](docs/models/AccountingMethod.md)
 - [ActionId](docs/models/ActionId.md)
 - [AddBusinessDaysToDateRequest](docs/models/AddBusinessDaysToDateRequest.md)
 - [AddBusinessDaysToDateResponse](docs/models/AddBusinessDaysToDateResponse.md)
 - [AdjustHolding](docs/models/AdjustHolding.md)
 - [AdjustHoldingRequest](docs/models/AdjustHoldingRequest.md)
 - [AggregateSpec](docs/models/AggregateSpec.md)
 - [AggregatedReturn](docs/models/AggregatedReturn.md)
 - [AggregatedReturnsRequest](docs/models/AggregatedReturnsRequest.md)
 - [AggregationContext](docs/models/AggregationContext.md)
 - [AggregationMeasureFailureDetail](docs/models/AggregationMeasureFailureDetail.md)
 - [AggregationOp](docs/models/AggregationOp.md)
 - [AggregationOptions](docs/models/AggregationOptions.md)
 - [AggregationQuery](docs/models/AggregationQuery.md)
 - [AggregationType](docs/models/AggregationType.md)
 - [Allocation](docs/models/Allocation.md)
 - [AllocationRequest](docs/models/AllocationRequest.md)
 - [AllocationSetRequest](docs/models/AllocationSetRequest.md)
 - [AnnulQuotesResponse](docs/models/AnnulQuotesResponse.md)
 - [AnnulSingleStructuredDataResponse](docs/models/AnnulSingleStructuredDataResponse.md)
 - [AnnulStructuredDataResponse](docs/models/AnnulStructuredDataResponse.md)
 - [AssetClass](docs/models/AssetClass.md)
 - [AtomValue](docs/models/AtomValue.md)
 - [AtomValue0D](docs/models/AtomValue0D.md)
 - [AtomValueDecimal](docs/models/AtomValueDecimal.md)
 - [AtomValueInt](docs/models/AtomValueInt.md)
 - [AtomValueString](docs/models/AtomValueString.md)
 - [AtomValueType](docs/models/AtomValueType.md)
 - [Basket](docs/models/Basket.md)
 - [BasketIdentifier](docs/models/BasketIdentifier.md)
 - [Block](docs/models/Block.md)
 - [BlockRequest](docs/models/BlockRequest.md)
 - [BlockSetRequest](docs/models/BlockSetRequest.md)
 - [Bond](docs/models/Bond.md)
 - [BucketedCashFlowRequest](docs/models/BucketedCashFlowRequest.md)
 - [BucketedCashFlowResponse](docs/models/BucketedCashFlowResponse.md)
 - [CalculationInfo](docs/models/CalculationInfo.md)
 - [CalculationMethod](docs/models/CalculationMethod.md)
 - [Calendar](docs/models/Calendar.md)
 - [CalendarDate](docs/models/CalendarDate.md)
 - [CapFloor](docs/models/CapFloor.md)
 - [CashLadderRecord](docs/models/CashLadderRecord.md)
 - [CashPerpetual](docs/models/CashPerpetual.md)
 - [CdsFlowConventions](docs/models/CdsFlowConventions.md)
 - [CdsIndex](docs/models/CdsIndex.md)
 - [CdsProtectionDetailSpecification](docs/models/CdsProtectionDetailSpecification.md)
 - [CdsRestructuringType](docs/models/CdsRestructuringType.md)
 - [CdsSeniority](docs/models/CdsSeniority.md)
 - [Change](docs/models/Change.md)
 - [CompletePortfolio](docs/models/CompletePortfolio.md)
 - [CompleteRelation](docs/models/CompleteRelation.md)
 - [CompleteRelationship](docs/models/CompleteRelationship.md)
 - [ComplexMarketData](docs/models/ComplexMarketData.md)
 - [ComplexMarketDataId](docs/models/ComplexMarketDataId.md)
 - [ComplianceRuleResult](docs/models/ComplianceRuleResult.md)
 - [ComplianceRun](docs/models/ComplianceRun.md)
 - [Compounding](docs/models/Compounding.md)
 - [ConfigurationRecipe](docs/models/ConfigurationRecipe.md)
 - [ConfigurationRecipeSnippet](docs/models/ConfigurationRecipeSnippet.md)
 - [ConstituentsAdjustmentHeader](docs/models/ConstituentsAdjustmentHeader.md)
 - [ContractForDifference](docs/models/ContractForDifference.md)
 - [CorporateAction](docs/models/CorporateAction.md)
 - [CorporateActionSource](docs/models/CorporateActionSource.md)
 - [CorporateActionTransition](docs/models/CorporateActionTransition.md)
 - [CorporateActionTransitionComponent](docs/models/CorporateActionTransitionComponent.md)
 - [CorporateActionTransitionComponentRequest](docs/models/CorporateActionTransitionComponentRequest.md)
 - [CorporateActionTransitionRequest](docs/models/CorporateActionTransitionRequest.md)
 - [CounterpartyAgreement](docs/models/CounterpartyAgreement.md)
 - [CounterpartyRiskInformation](docs/models/CounterpartyRiskInformation.md)
 - [CounterpartySignatory](docs/models/CounterpartySignatory.md)
 - [CreateCalendarRequest](docs/models/CreateCalendarRequest.md)
 - [CreateCorporateActionSourceRequest](docs/models/CreateCorporateActionSourceRequest.md)
 - [CreateCutLabelDefinitionRequest](docs/models/CreateCutLabelDefinitionRequest.md)
 - [CreateDataMapRequest](docs/models/CreateDataMapRequest.md)
 - [CreateDataTypeRequest](docs/models/CreateDataTypeRequest.md)
 - [CreateDateRequest](docs/models/CreateDateRequest.md)
 - [CreateDerivedPropertyDefinitionRequest](docs/models/CreateDerivedPropertyDefinitionRequest.md)
 - [CreateDerivedTransactionPortfolioRequest](docs/models/CreateDerivedTransactionPortfolioRequest.md)
 - [CreatePortfolioDetails](docs/models/CreatePortfolioDetails.md)
 - [CreatePortfolioGroupRequest](docs/models/CreatePortfolioGroupRequest.md)
 - [CreatePropertyDefinitionRequest](docs/models/CreatePropertyDefinitionRequest.md)
 - [CreateRecipeRequest](docs/models/CreateRecipeRequest.md)
 - [CreateReferencePortfolioRequest](docs/models/CreateReferencePortfolioRequest.md)
 - [CreateRelationDefinitionRequest](docs/models/CreateRelationDefinitionRequest.md)
 - [CreateRelationRequest](docs/models/CreateRelationRequest.md)
 - [CreateRelationshipDefinitionRequest](docs/models/CreateRelationshipDefinitionRequest.md)
 - [CreateRelationshipRequest](docs/models/CreateRelationshipRequest.md)
 - [CreateSequenceRequest](docs/models/CreateSequenceRequest.md)
 - [CreateTransactionPortfolioRequest](docs/models/CreateTransactionPortfolioRequest.md)
 - [CreateUnitDefinition](docs/models/CreateUnitDefinition.md)
 - [CreditDefaultSwap](docs/models/CreditDefaultSwap.md)
 - [CreditRating](docs/models/CreditRating.md)
 - [CreditSpreadCurveData](docs/models/CreditSpreadCurveData.md)
 - [CreditSupportAnnex](docs/models/CreditSupportAnnex.md)
 - [CrossCurrencySwap](docs/models/CrossCurrencySwap.md)
 - [CurrencyAndAmount](docs/models/CurrencyAndAmount.md)
 - [CustomEntityDefinition](docs/models/CustomEntityDefinition.md)
 - [CustomEntityDefinitionRequest](docs/models/CustomEntityDefinitionRequest.md)
 - [CustomEntityField](docs/models/CustomEntityField.md)
 - [CustomEntityFieldDefinition](docs/models/CustomEntityFieldDefinition.md)
 - [CustomEntityIdRequest](docs/models/CustomEntityIdRequest.md)
 - [CustomEntityIdResponse](docs/models/CustomEntityIdResponse.md)
 - [CustomEntityRequest](docs/models/CustomEntityRequest.md)
 - [CustomEntityResponse](docs/models/CustomEntityResponse.md)
 - [CutLabelDefinition](docs/models/CutLabelDefinition.md)
 - [CutLocalTime](docs/models/CutLocalTime.md)
 - [DataDefinition](docs/models/DataDefinition.md)
 - [DataMapKey](docs/models/DataMapKey.md)
 - [DataMapping](docs/models/DataMapping.md)
 - [DataType](docs/models/DataType.md)
 - [DataTypeSummary](docs/models/DataTypeSummary.md)
 - [DataTypeValueRange](docs/models/DataTypeValueRange.md)
 - [DateAttributes](docs/models/DateAttributes.md)
 - [DateRange](docs/models/DateRange.md)
 - [DateTimeComparisonType](docs/models/DateTimeComparisonType.md)
 - [DayOfWeek](docs/models/DayOfWeek.md)
 - [DeleteInstrumentPropertiesResponse](docs/models/DeleteInstrumentPropertiesResponse.md)
 - [DeleteInstrumentResponse](docs/models/DeleteInstrumentResponse.md)
 - [DeleteRelationRequest](docs/models/DeleteRelationRequest.md)
 - [DeleteRelationshipRequest](docs/models/DeleteRelationshipRequest.md)
 - [DeletedEntityResponse](docs/models/DeletedEntityResponse.md)
 - [DeliveryType](docs/models/DeliveryType.md)
 - [DiscountFactorCurveData](docs/models/DiscountFactorCurveData.md)
 - [DiscountingMethod](docs/models/DiscountingMethod.md)
 - [EmptyModelOptions](docs/models/EmptyModelOptions.md)
 - [Equity](docs/models/Equity.md)
 - [EquityOption](docs/models/EquityOption.md)
 - [EquitySwap](docs/models/EquitySwap.md)
 - [EquityVolSurfaceData](docs/models/EquityVolSurfaceData.md)
 - [ErrorDetail](docs/models/ErrorDetail.md)
 - [ExchangeTradedOption](docs/models/ExchangeTradedOption.md)
 - [ExchangeTradedOptionContractDetails](docs/models/ExchangeTradedOptionContractDetails.md)
 - [Execution](docs/models/Execution.md)
 - [ExecutionRequest](docs/models/ExecutionRequest.md)
 - [ExecutionSetRequest](docs/models/ExecutionSetRequest.md)
 - [ExoticInstrument](docs/models/ExoticInstrument.md)
 - [ExpandedGroup](docs/models/ExpandedGroup.md)
 - [FeeCalculationDetails](docs/models/FeeCalculationDetails.md)
 - [FieldDefinition](docs/models/FieldDefinition.md)
 - [FieldSchema](docs/models/FieldSchema.md)
 - [FieldValue](docs/models/FieldValue.md)
 - [FileResponse](docs/models/FileResponse.md)
 - [FixedLeg](docs/models/FixedLeg.md)
 - [FloatingLeg](docs/models/FloatingLeg.md)
 - [FlowConventionName](docs/models/FlowConventionName.md)
 - [FlowConventions](docs/models/FlowConventions.md)
 - [ForwardRateAgreement](docs/models/ForwardRateAgreement.md)
 - [FundingLeg](docs/models/FundingLeg.md)
 - [Future](docs/models/Future.md)
 - [FuturesContractDetails](docs/models/FuturesContractDetails.md)
 - [FxForward](docs/models/FxForward.md)
 - [FxForwardCurveByQuoteReference](docs/models/FxForwardCurveByQuoteReference.md)
 - [FxForwardCurveData](docs/models/FxForwardCurveData.md)
 - [FxForwardModelOptions](docs/models/FxForwardModelOptions.md)
 - [FxForwardPipsCurveData](docs/models/FxForwardPipsCurveData.md)
 - [FxForwardTenorCurveData](docs/models/FxForwardTenorCurveData.md)
 - [FxForwardTenorPipsCurveData](docs/models/FxForwardTenorPipsCurveData.md)
 - [FxOption](docs/models/FxOption.md)
 - [FxSwap](docs/models/FxSwap.md)
 - [FxVolSurfaceData](docs/models/FxVolSurfaceData.md)
 - [GetCdsFlowConventionsResponse](docs/models/GetCdsFlowConventionsResponse.md)
 - [GetComplexMarketDataResponse](docs/models/GetComplexMarketDataResponse.md)
 - [GetCounterpartyAgreementResponse](docs/models/GetCounterpartyAgreementResponse.md)
 - [GetCreditSupportAnnexResponse](docs/models/GetCreditSupportAnnexResponse.md)
 - [GetDataMapResponse](docs/models/GetDataMapResponse.md)
 - [GetFlowConventionsResponse](docs/models/GetFlowConventionsResponse.md)
 - [GetIndexConventionResponse](docs/models/GetIndexConventionResponse.md)
 - [GetInstrumentsResponse](docs/models/GetInstrumentsResponse.md)
 - [GetQuotesResponse](docs/models/GetQuotesResponse.md)
 - [GetRecipeResponse](docs/models/GetRecipeResponse.md)
 - [GetReferencePortfolioConstituentsResponse](docs/models/GetReferencePortfolioConstituentsResponse.md)
 - [GetStructuredResultDataResponse](docs/models/GetStructuredResultDataResponse.md)
 - [GetVirtualDocumentResponse](docs/models/GetVirtualDocumentResponse.md)
 - [GroupedResultOfAddressKey](docs/models/GroupedResultOfAddressKey.md)
 - [HoldingAdjustment](docs/models/HoldingAdjustment.md)
 - [HoldingContext](docs/models/HoldingContext.md)
 - [HoldingsAdjustment](docs/models/HoldingsAdjustment.md)
 - [HoldingsAdjustmentHeader](docs/models/HoldingsAdjustmentHeader.md)
 - [IDataRecord](docs/models/IDataRecord.md)
 - [IUnitDefinitionDto](docs/models/IUnitDefinitionDto.md)
 - [IdSelectorDefinition](docs/models/IdSelectorDefinition.md)
 - [IdentifierPartSchema](docs/models/IdentifierPartSchema.md)
 - [IndexConvention](docs/models/IndexConvention.md)
 - [IndexModelOptions](docs/models/IndexModelOptions.md)
 - [IndustryClassifier](docs/models/IndustryClassifier.md)
 - [InlineValuationRequest](docs/models/InlineValuationRequest.md)
 - [InlineValuationsReconciliationRequest](docs/models/InlineValuationsReconciliationRequest.md)
 - [Instrument](docs/models/Instrument.md)
 - [InstrumentCashFlow](docs/models/InstrumentCashFlow.md)
 - [InstrumentDefinition](docs/models/InstrumentDefinition.md)
 - [InstrumentDefinitionFormat](docs/models/InstrumentDefinitionFormat.md)
 - [InstrumentIdTypeDescriptor](docs/models/InstrumentIdTypeDescriptor.md)
 - [InstrumentIdValue](docs/models/InstrumentIdValue.md)
 - [InstrumentLeg](docs/models/InstrumentLeg.md)
 - [InstrumentMatch](docs/models/InstrumentMatch.md)
 - [InstrumentProperties](docs/models/InstrumentProperties.md)
 - [InstrumentSearchProperty](docs/models/InstrumentSearchProperty.md)
 - [InstrumentType](docs/models/InstrumentType.md)
 - [InterestRateSwap](docs/models/InterestRateSwap.md)
 - [InterestRateSwaption](docs/models/InterestRateSwaption.md)
 - [IrVolCubeData](docs/models/IrVolCubeData.md)
 - [IsBusinessDayResponse](docs/models/IsBusinessDayResponse.md)
 - [LabelValueSet](docs/models/LabelValueSet.md)
 - [LegDefinition](docs/models/LegDefinition.md)
 - [LegalEntity](docs/models/LegalEntity.md)
 - [LevelStep](docs/models/LevelStep.md)
 - [Link](docs/models/Link.md)
 - [ListAggregationReconciliation](docs/models/ListAggregationReconciliation.md)
 - [ListAggregationResponse](docs/models/ListAggregationResponse.md)
 - [ListComplexMarketDataWithMetaDataResponse](docs/models/ListComplexMarketDataWithMetaDataResponse.md)
 - [LusidInstrument](docs/models/LusidInstrument.md)
 - [LusidProblemDetails](docs/models/LusidProblemDetails.md)
 - [LusidValidationProblemDetails](docs/models/LusidValidationProblemDetails.md)
 - [MarketContext](docs/models/MarketContext.md)
 - [MarketDataKeyRule](docs/models/MarketDataKeyRule.md)
 - [MarketDataType](docs/models/MarketDataType.md)
 - [MarketIdentifier](docs/models/MarketIdentifier.md)
 - [MarketObservableType](docs/models/MarketObservableType.md)
 - [MarketOptions](docs/models/MarketOptions.md)
 - [MarketQuote](docs/models/MarketQuote.md)
 - [MetricValue](docs/models/MetricValue.md)
 - [ModelOptions](docs/models/ModelOptions.md)
 - [ModelOptionsType](docs/models/ModelOptionsType.md)
 - [ModelProperty](docs/models/ModelProperty.md)
 - [ModelSelection](docs/models/ModelSelection.md)
 - [MovementType](docs/models/MovementType.md)
 - [Multiplier](docs/models/Multiplier.md)
 - [NextValueInSequenceResponse](docs/models/NextValueInSequenceResponse.md)
 - [NumericComparisonType](docs/models/NumericComparisonType.md)
 - [OpaqueMarketData](docs/models/OpaqueMarketData.md)
 - [OpaqueModelOptions](docs/models/OpaqueModelOptions.md)
 - [OperandType](docs/models/OperandType.md)
 - [Operation](docs/models/Operation.md)
 - [Operator](docs/models/Operator.md)
 - [OptionType](docs/models/OptionType.md)
 - [Order](docs/models/Order.md)
 - [OrderBySpec](docs/models/OrderBySpec.md)
 - [OrderGraphBlock](docs/models/OrderGraphBlock.md)
 - [OrderGraphPlacement](docs/models/OrderGraphPlacement.md)
 - [OrderGraphSynopsis](docs/models/OrderGraphSynopsis.md)
 - [OrderInstruction](docs/models/OrderInstruction.md)
 - [OrderInstructionRequest](docs/models/OrderInstructionRequest.md)
 - [OrderInstructionSetRequest](docs/models/OrderInstructionSetRequest.md)
 - [OrderRequest](docs/models/OrderRequest.md)
 - [OrderSetRequest](docs/models/OrderSetRequest.md)
 - [OtcConfirmation](docs/models/OtcConfirmation.md)
 - [OutputTransaction](docs/models/OutputTransaction.md)
 - [Package](docs/models/Package.md)
 - [PackageRequest](docs/models/PackageRequest.md)
 - [PackageSetRequest](docs/models/PackageSetRequest.md)
 - [PagedResourceListOfAllocation](docs/models/PagedResourceListOfAllocation.md)
 - [PagedResourceListOfBlock](docs/models/PagedResourceListOfBlock.md)
 - [PagedResourceListOfCalendar](docs/models/PagedResourceListOfCalendar.md)
 - [PagedResourceListOfComplianceRuleResult](docs/models/PagedResourceListOfComplianceRuleResult.md)
 - [PagedResourceListOfComplianceRun](docs/models/PagedResourceListOfComplianceRun.md)
 - [PagedResourceListOfCorporateActionSource](docs/models/PagedResourceListOfCorporateActionSource.md)
 - [PagedResourceListOfCustomEntityResponse](docs/models/PagedResourceListOfCustomEntityResponse.md)
 - [PagedResourceListOfCutLabelDefinition](docs/models/PagedResourceListOfCutLabelDefinition.md)
 - [PagedResourceListOfDataTypeSummary](docs/models/PagedResourceListOfDataTypeSummary.md)
 - [PagedResourceListOfExecution](docs/models/PagedResourceListOfExecution.md)
 - [PagedResourceListOfInstrument](docs/models/PagedResourceListOfInstrument.md)
 - [PagedResourceListOfLegalEntity](docs/models/PagedResourceListOfLegalEntity.md)
 - [PagedResourceListOfOrder](docs/models/PagedResourceListOfOrder.md)
 - [PagedResourceListOfOrderGraphBlock](docs/models/PagedResourceListOfOrderGraphBlock.md)
 - [PagedResourceListOfOrderGraphPlacement](docs/models/PagedResourceListOfOrderGraphPlacement.md)
 - [PagedResourceListOfOrderInstruction](docs/models/PagedResourceListOfOrderInstruction.md)
 - [PagedResourceListOfPackage](docs/models/PagedResourceListOfPackage.md)
 - [PagedResourceListOfParticipation](docs/models/PagedResourceListOfParticipation.md)
 - [PagedResourceListOfPerson](docs/models/PagedResourceListOfPerson.md)
 - [PagedResourceListOfPlacement](docs/models/PagedResourceListOfPlacement.md)
 - [PagedResourceListOfPortfolioGroupSearchResult](docs/models/PagedResourceListOfPortfolioGroupSearchResult.md)
 - [PagedResourceListOfPortfolioSearchResult](docs/models/PagedResourceListOfPortfolioSearchResult.md)
 - [PagedResourceListOfPropertyDefinitionSearchResult](docs/models/PagedResourceListOfPropertyDefinitionSearchResult.md)
 - [PagedResourceListOfRelationshipDefinition](docs/models/PagedResourceListOfRelationshipDefinition.md)
 - [PagedResourceListOfSequenceDefinition](docs/models/PagedResourceListOfSequenceDefinition.md)
 - [Participation](docs/models/Participation.md)
 - [ParticipationRequest](docs/models/ParticipationRequest.md)
 - [ParticipationSetRequest](docs/models/ParticipationSetRequest.md)
 - [PerformanceReturn](docs/models/PerformanceReturn.md)
 - [PerformanceReturnsMetric](docs/models/PerformanceReturnsMetric.md)
 - [PeriodType](docs/models/PeriodType.md)
 - [PerpetualEntityState](docs/models/PerpetualEntityState.md)
 - [PerpetualProperty](docs/models/PerpetualProperty.md)
 - [Person](docs/models/Person.md)
 - [Placement](docs/models/Placement.md)
 - [PlacementRequest](docs/models/PlacementRequest.md)
 - [PlacementSetRequest](docs/models/PlacementSetRequest.md)
 - [Portfolio](docs/models/Portfolio.md)
 - [PortfolioCashFlow](docs/models/PortfolioCashFlow.md)
 - [PortfolioCashLadder](docs/models/PortfolioCashLadder.md)
 - [PortfolioDetails](docs/models/PortfolioDetails.md)
 - [PortfolioEntityId](docs/models/PortfolioEntityId.md)
 - [PortfolioGroup](docs/models/PortfolioGroup.md)
 - [PortfolioGroupProperties](docs/models/PortfolioGroupProperties.md)
 - [PortfolioGroupSearchResult](docs/models/PortfolioGroupSearchResult.md)
 - [PortfolioHolding](docs/models/PortfolioHolding.md)
 - [PortfolioProperties](docs/models/PortfolioProperties.md)
 - [PortfolioReconciliationRequest](docs/models/PortfolioReconciliationRequest.md)
 - [PortfolioSearchResult](docs/models/PortfolioSearchResult.md)
 - [PortfolioType](docs/models/PortfolioType.md)
 - [PortfoliosReconciliationRequest](docs/models/PortfoliosReconciliationRequest.md)
 - [PortfoliosReconciliationRequestPreview](docs/models/PortfoliosReconciliationRequestPreview.md)
 - [Premium](docs/models/Premium.md)
 - [PricingContext](docs/models/PricingContext.md)
 - [PricingModel](docs/models/PricingModel.md)
 - [PricingOptions](docs/models/PricingOptions.md)
 - [ProcessedCommand](docs/models/ProcessedCommand.md)
 - [PropertyDefinition](docs/models/PropertyDefinition.md)
 - [PropertyDefinitionSearchResult](docs/models/PropertyDefinitionSearchResult.md)
 - [PropertyDefinitionType](docs/models/PropertyDefinitionType.md)
 - [PropertyDomain](docs/models/PropertyDomain.md)
 - [PropertyFilter](docs/models/PropertyFilter.md)
 - [PropertyInterval](docs/models/PropertyInterval.md)
 - [PropertyLifeTime](docs/models/PropertyLifeTime.md)
 - [PropertySchema](docs/models/PropertySchema.md)
 - [PropertyType](docs/models/PropertyType.md)
 - [PropertyValue](docs/models/PropertyValue.md)
 - [Quote](docs/models/Quote.md)
 - [QuoteAccessMetadataRule](docs/models/QuoteAccessMetadataRule.md)
 - [QuoteAccessMetadataRuleId](docs/models/QuoteAccessMetadataRuleId.md)
 - [QuoteId](docs/models/QuoteId.md)
 - [QuoteInstrumentIdType](docs/models/QuoteInstrumentIdType.md)
 - [QuoteSeriesId](docs/models/QuoteSeriesId.md)
 - [QuoteType](docs/models/QuoteType.md)
 - [RealisedGainLoss](docs/models/RealisedGainLoss.md)
 - [ReconcileDateTimeRule](docs/models/ReconcileDateTimeRule.md)
 - [ReconcileNumericRule](docs/models/ReconcileNumericRule.md)
 - [ReconcileStringRule](docs/models/ReconcileStringRule.md)
 - [ReconciliationBreak](docs/models/ReconciliationBreak.md)
 - [ReconciliationLeftRightAddressKeyPair](docs/models/ReconciliationLeftRightAddressKeyPair.md)
 - [ReconciliationLine](docs/models/ReconciliationLine.md)
 - [ReconciliationRequest](docs/models/ReconciliationRequest.md)
 - [ReconciliationResponse](docs/models/ReconciliationResponse.md)
 - [ReconciliationRule](docs/models/ReconciliationRule.md)
 - [ReconciliationRuleType](docs/models/ReconciliationRuleType.md)
 - [ReferenceData](docs/models/ReferenceData.md)
 - [ReferencePortfolioConstituent](docs/models/ReferencePortfolioConstituent.md)
 - [ReferencePortfolioConstituentRequest](docs/models/ReferencePortfolioConstituentRequest.md)
 - [ReferencePortfolioWeightType](docs/models/ReferencePortfolioWeightType.md)
 - [RelatedEntity](docs/models/RelatedEntity.md)
 - [Relation](docs/models/Relation.md)
 - [RelationDefinition](docs/models/RelationDefinition.md)
 - [Relationship](docs/models/Relationship.md)
 - [RelationshipDefinition](docs/models/RelationshipDefinition.md)
 - [Repo](docs/models/Repo.md)
 - [ResourceId](docs/models/ResourceId.md)
 - [ResourceListOfAccessControlledResource](docs/models/ResourceListOfAccessControlledResource.md)
 - [ResourceListOfAccessMetadataValueOf](docs/models/ResourceListOfAccessMetadataValueOf.md)
 - [ResourceListOfAggregatedReturn](docs/models/ResourceListOfAggregatedReturn.md)
 - [ResourceListOfAggregationQuery](docs/models/ResourceListOfAggregationQuery.md)
 - [ResourceListOfAllocation](docs/models/ResourceListOfAllocation.md)
 - [ResourceListOfBlock](docs/models/ResourceListOfBlock.md)
 - [ResourceListOfCalendarDate](docs/models/ResourceListOfCalendarDate.md)
 - [ResourceListOfChange](docs/models/ResourceListOfChange.md)
 - [ResourceListOfConstituentsAdjustmentHeader](docs/models/ResourceListOfConstituentsAdjustmentHeader.md)
 - [ResourceListOfCorporateAction](docs/models/ResourceListOfCorporateAction.md)
 - [ResourceListOfDataType](docs/models/ResourceListOfDataType.md)
 - [ResourceListOfExecution](docs/models/ResourceListOfExecution.md)
 - [ResourceListOfFeeCalculationDetails](docs/models/ResourceListOfFeeCalculationDetails.md)
 - [ResourceListOfGetCdsFlowConventionsResponse](docs/models/ResourceListOfGetCdsFlowConventionsResponse.md)
 - [ResourceListOfGetCounterpartyAgreementResponse](docs/models/ResourceListOfGetCounterpartyAgreementResponse.md)
 - [ResourceListOfGetCreditSupportAnnexResponse](docs/models/ResourceListOfGetCreditSupportAnnexResponse.md)
 - [ResourceListOfGetFlowConventionsResponse](docs/models/ResourceListOfGetFlowConventionsResponse.md)
 - [ResourceListOfGetIndexConventionResponse](docs/models/ResourceListOfGetIndexConventionResponse.md)
 - [ResourceListOfGetRecipeResponse](docs/models/ResourceListOfGetRecipeResponse.md)
 - [ResourceListOfHoldingsAdjustmentHeader](docs/models/ResourceListOfHoldingsAdjustmentHeader.md)
 - [ResourceListOfIUnitDefinitionDto](docs/models/ResourceListOfIUnitDefinitionDto.md)
 - [ResourceListOfInstrumentCashFlow](docs/models/ResourceListOfInstrumentCashFlow.md)
 - [ResourceListOfInstrumentIdTypeDescriptor](docs/models/ResourceListOfInstrumentIdTypeDescriptor.md)
 - [ResourceListOfListComplexMarketDataWithMetaDataResponse](docs/models/ResourceListOfListComplexMarketDataWithMetaDataResponse.md)
 - [ResourceListOfOrder](docs/models/ResourceListOfOrder.md)
 - [ResourceListOfOrderInstruction](docs/models/ResourceListOfOrderInstruction.md)
 - [ResourceListOfPackage](docs/models/ResourceListOfPackage.md)
 - [ResourceListOfParticipation](docs/models/ResourceListOfParticipation.md)
 - [ResourceListOfPerformanceReturn](docs/models/ResourceListOfPerformanceReturn.md)
 - [ResourceListOfPlacement](docs/models/ResourceListOfPlacement.md)
 - [ResourceListOfPortfolio](docs/models/ResourceListOfPortfolio.md)
 - [ResourceListOfPortfolioCashFlow](docs/models/ResourceListOfPortfolioCashFlow.md)
 - [ResourceListOfPortfolioCashLadder](docs/models/ResourceListOfPortfolioCashLadder.md)
 - [ResourceListOfPortfolioGroup](docs/models/ResourceListOfPortfolioGroup.md)
 - [ResourceListOfProcessedCommand](docs/models/ResourceListOfProcessedCommand.md)
 - [ResourceListOfProperty](docs/models/ResourceListOfProperty.md)
 - [ResourceListOfPropertyDefinition](docs/models/ResourceListOfPropertyDefinition.md)
 - [ResourceListOfPropertyInterval](docs/models/ResourceListOfPropertyInterval.md)
 - [ResourceListOfQuote](docs/models/ResourceListOfQuote.md)
 - [ResourceListOfQuoteAccessMetadataRule](docs/models/ResourceListOfQuoteAccessMetadataRule.md)
 - [ResourceListOfReconciliationBreak](docs/models/ResourceListOfReconciliationBreak.md)
 - [ResourceListOfRelation](docs/models/ResourceListOfRelation.md)
 - [ResourceListOfRelationship](docs/models/ResourceListOfRelationship.md)
 - [ResourceListOfScopeDefinition](docs/models/ResourceListOfScopeDefinition.md)
 - [ResourceListOfString](docs/models/ResourceListOfString.md)
 - [ResourceListOfTransaction](docs/models/ResourceListOfTransaction.md)
 - [ResourceListOfValueType](docs/models/ResourceListOfValueType.md)
 - [ResultDataKeyRule](docs/models/ResultDataKeyRule.md)
 - [ResultDataSchema](docs/models/ResultDataSchema.md)
 - [ScalingMethodology](docs/models/ScalingMethodology.md)
 - [Schema](docs/models/Schema.md)
 - [ScopeDefinition](docs/models/ScopeDefinition.md)
 - [SequenceDefinition](docs/models/SequenceDefinition.md)
 - [SetLegalEntityIdentifiersRequest](docs/models/SetLegalEntityIdentifiersRequest.md)
 - [SetPersonIdentifiersRequest](docs/models/SetPersonIdentifiersRequest.md)
 - [SetPersonPropertiesRequest](docs/models/SetPersonPropertiesRequest.md)
 - [SetTransactionConfigurationAlias](docs/models/SetTransactionConfigurationAlias.md)
 - [SetTransactionConfigurationSourceRequest](docs/models/SetTransactionConfigurationSourceRequest.md)
 - [SideConfigurationData](docs/models/SideConfigurationData.md)
 - [SideConfigurationDataRequest](docs/models/SideConfigurationDataRequest.md)
 - [SimpleInstrument](docs/models/SimpleInstrument.md)
 - [SortOrder](docs/models/SortOrder.md)
 - [StepSchedule](docs/models/StepSchedule.md)
 - [Stream](docs/models/Stream.md)
 - [StringComparisonType](docs/models/StringComparisonType.md)
 - [StructuredResultData](docs/models/StructuredResultData.md)
 - [StructuredResultDataId](docs/models/StructuredResultDataId.md)
 - [TargetTaxLot](docs/models/TargetTaxLot.md)
 - [TargetTaxLotRequest](docs/models/TargetTaxLotRequest.md)
 - [TermDeposit](docs/models/TermDeposit.md)
 - [Tolerance](docs/models/Tolerance.md)
 - [ToleranceEnum](docs/models/ToleranceEnum.md)
 - [Transaction](docs/models/Transaction.md)
 - [TransactionConfigurationData](docs/models/TransactionConfigurationData.md)
 - [TransactionConfigurationDataRequest](docs/models/TransactionConfigurationDataRequest.md)
 - [TransactionConfigurationMovementData](docs/models/TransactionConfigurationMovementData.md)
 - [TransactionConfigurationMovementDataRequest](docs/models/TransactionConfigurationMovementDataRequest.md)
 - [TransactionConfigurationTypeAlias](docs/models/TransactionConfigurationTypeAlias.md)
 - [TransactionPrice](docs/models/TransactionPrice.md)
 - [TransactionPriceType](docs/models/TransactionPriceType.md)
 - [TransactionPropertyMapping](docs/models/TransactionPropertyMapping.md)
 - [TransactionPropertyMappingRequest](docs/models/TransactionPropertyMappingRequest.md)
 - [TransactionQueryMode](docs/models/TransactionQueryMode.md)
 - [TransactionQueryParameters](docs/models/TransactionQueryParameters.md)
 - [TransactionRequest](docs/models/TransactionRequest.md)
 - [TransactionRoles](docs/models/TransactionRoles.md)
 - [TransactionSetConfigurationData](docs/models/TransactionSetConfigurationData.md)
 - [TransactionSetConfigurationDataRequest](docs/models/TransactionSetConfigurationDataRequest.md)
 - [TransactionStatus](docs/models/TransactionStatus.md)
 - [TranslateInstrumentDefinitionsRequest](docs/models/TranslateInstrumentDefinitionsRequest.md)
 - [TranslateInstrumentDefinitionsResponse](docs/models/TranslateInstrumentDefinitionsResponse.md)
 - [TypedResourceId](docs/models/TypedResourceId.md)
 - [UnitSchema](docs/models/UnitSchema.md)
 - [UnmatchedHoldingMethod](docs/models/UnmatchedHoldingMethod.md)
 - [UpdateCalendarRequest](docs/models/UpdateCalendarRequest.md)
 - [UpdateCutLabelDefinitionRequest](docs/models/UpdateCutLabelDefinitionRequest.md)
 - [UpdateDataTypeRequest](docs/models/UpdateDataTypeRequest.md)
 - [UpdateInstrumentIdentifierRequest](docs/models/UpdateInstrumentIdentifierRequest.md)
 - [UpdatePortfolioGroupRequest](docs/models/UpdatePortfolioGroupRequest.md)
 - [UpdatePortfolioRequest](docs/models/UpdatePortfolioRequest.md)
 - [UpdatePropertyDefinitionRequest](docs/models/UpdatePropertyDefinitionRequest.md)
 - [UpdateRelationshipDefinitionRequest](docs/models/UpdateRelationshipDefinitionRequest.md)
 - [UpdateUnitRequest](docs/models/UpdateUnitRequest.md)
 - [UpsertCdsFlowConventionsRequest](docs/models/UpsertCdsFlowConventionsRequest.md)
 - [UpsertComplexMarketDataRequest](docs/models/UpsertComplexMarketDataRequest.md)
 - [UpsertCorporateActionRequest](docs/models/UpsertCorporateActionRequest.md)
 - [UpsertCorporateActionsResponse](docs/models/UpsertCorporateActionsResponse.md)
 - [UpsertCounterpartyAgreementRequest](docs/models/UpsertCounterpartyAgreementRequest.md)
 - [UpsertCreditSupportAnnexRequest](docs/models/UpsertCreditSupportAnnexRequest.md)
 - [UpsertFlowConventionsRequest](docs/models/UpsertFlowConventionsRequest.md)
 - [UpsertIndexConventionRequest](docs/models/UpsertIndexConventionRequest.md)
 - [UpsertInstrumentPropertiesResponse](docs/models/UpsertInstrumentPropertiesResponse.md)
 - [UpsertInstrumentPropertyRequest](docs/models/UpsertInstrumentPropertyRequest.md)
 - [UpsertInstrumentsResponse](docs/models/UpsertInstrumentsResponse.md)
 - [UpsertLegalEntityAccessMetadataRequest](docs/models/UpsertLegalEntityAccessMetadataRequest.md)
 - [UpsertLegalEntityRequest](docs/models/UpsertLegalEntityRequest.md)
 - [UpsertPersonAccessMetadataRequest](docs/models/UpsertPersonAccessMetadataRequest.md)
 - [UpsertPersonRequest](docs/models/UpsertPersonRequest.md)
 - [UpsertPortfolioAccessMetadataRequest](docs/models/UpsertPortfolioAccessMetadataRequest.md)
 - [UpsertPortfolioGroupAccessMetadataRequest](docs/models/UpsertPortfolioGroupAccessMetadataRequest.md)
 - [UpsertPortfolioTransactionsResponse](docs/models/UpsertPortfolioTransactionsResponse.md)
 - [UpsertQuoteAccessMetadataRuleRequest](docs/models/UpsertQuoteAccessMetadataRuleRequest.md)
 - [UpsertQuoteRequest](docs/models/UpsertQuoteRequest.md)
 - [UpsertQuotesResponse](docs/models/UpsertQuotesResponse.md)
 - [UpsertRecipeRequest](docs/models/UpsertRecipeRequest.md)
 - [UpsertReferencePortfolioConstituentsRequest](docs/models/UpsertReferencePortfolioConstituentsRequest.md)
 - [UpsertReferencePortfolioConstituentsResponse](docs/models/UpsertReferencePortfolioConstituentsResponse.md)
 - [UpsertReturnsResponse](docs/models/UpsertReturnsResponse.md)
 - [UpsertSingleStructuredDataResponse](docs/models/UpsertSingleStructuredDataResponse.md)
 - [UpsertStructuredDataResponse](docs/models/UpsertStructuredDataResponse.md)
 - [UpsertStructuredResultDataRequest](docs/models/UpsertStructuredResultDataRequest.md)
 - [UpsertTransactionPropertiesResponse](docs/models/UpsertTransactionPropertiesResponse.md)
 - [User](docs/models/User.md)
 - [ValuationRequest](docs/models/ValuationRequest.md)
 - [ValuationSchedule](docs/models/ValuationSchedule.md)
 - [ValuationsReconciliationRequest](docs/models/ValuationsReconciliationRequest.md)
 - [ValueType](docs/models/ValueType.md)
 - [VendorLibrary](docs/models/VendorLibrary.md)
 - [VendorModelRule](docs/models/VendorModelRule.md)
 - [Version](docs/models/Version.md)
 - [VersionSummaryDto](docs/models/VersionSummaryDto.md)
 - [VersionedResourceListOfA2BDataRecord](docs/models/VersionedResourceListOfA2BDataRecord.md)
 - [VersionedResourceListOfA2BMovementRecord](docs/models/VersionedResourceListOfA2BMovementRecord.md)
 - [VersionedResourceListOfOutputTransaction](docs/models/VersionedResourceListOfOutputTransaction.md)
 - [VersionedResourceListOfPortfolioHolding](docs/models/VersionedResourceListOfPortfolioHolding.md)
 - [VersionedResourceListOfTransaction](docs/models/VersionedResourceListOfTransaction.md)
 - [VersionedResourceListWithWarningsOfPortfolioHolding](docs/models/VersionedResourceListWithWarningsOfPortfolioHolding.md)
 - [VirtualDocument](docs/models/VirtualDocument.md)
 - [VirtualDocumentRow](docs/models/VirtualDocumentRow.md)
 - [Warning](docs/models/Warning.md)
 - [WeekendMask](docs/models/WeekendMask.md)
 - [WeightedInstrument](docs/models/WeightedInstrument.md)
 - [WeightedInstruments](docs/models/WeightedInstruments.md)
 - [YieldCurveData](docs/models/YieldCurveData.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## oauth2

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://lusid.okta.com/oauth2/default/v1/authorize
- **Scopes**: N/A


## Author

info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in luisd.apis and luisd.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from luisd.apis.default_api import DefaultApi`
- `from luisd.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import luisd
from luisd.apis import *
from luisd.models import *
```
